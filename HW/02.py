import math
import random

citys = [
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def hillclimbing(citys, time):
    d = list(range(len(citys)))
    random.shuffle(d)
    d1 = pathLength(d)

    for _ in range(time):
        sortlen = d[:]
        i, j = random.sample(range(len(citys)), 2)
        sortlen[i], sortlen[j] = sortlen[j], sortlen[i]
        near = pathLength(sortlen)

        if near < d1:
            d = sortlen
            d1 = near
    return d

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i + 1) % plen]])
    return dist

result = hillclimbing(citys, time=10000)
print(result)
print(pathLength(result))
