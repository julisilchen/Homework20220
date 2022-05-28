with open('input.txt') as pieces:
    pieces = pieces.read().split('\n')

num = pieces[0].split()
p = pieces[1:]

from sys import setrecursionlimit # увеличивается глубина рекурсии

setrecursionlimit(100500)

n, m = int(num[0]), int(num[1])
p = pieces[1:]

field = {(x, y) for y in range(n) for x, c in enumerate(''.join(p)) if c == '#'} # формирует множство которое состоит из координат всех решёток

# рекурсия, которая формирует очертания фигуры и рекурсия, которая формирует очертания фигуры, удаляет значения из field
def dfs(xy):
    field.discard(xy)
    x, y = xy
    print(x,y)
    # смотрим соседние от точки значения. Если они есть в field, то идёт рекурсия
    for ij in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if ij in field:
            dfs(ij)

res = 0
# прогоняем, пока field не будет пустым
while field:
    dfs(field.pop())
    res += 1
print(res)