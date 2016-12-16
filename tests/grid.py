from decimal import *


density = 5
step = 1 / density
print(step)
getcontext().prec = 8
grid = []
for i in range(density):
    for j in range(density):
        for k in range(density):
            point = [k * step + step / 2, j * step + step / 2, i * step + step / 2]
            print(point)
            grid.append(point)

print(len(grid))
