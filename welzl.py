import random
from disc import *
import sys
sys.path.append('../geom')
from point import *

def minidiscwith2points(P, q1, q2, D):
    D[0] = disc(points = [q1, q2])
    n = len(P)
    for k in range(n):
        if D[k].inside(P[k]):
            D[k+1] = D[k]
        else:
            D[k+1] = disc(points=[q1, q2, P[k]])
    return D[n]

def minidiscwithpoint(P, q, D):
    D[0] = disc(points = [P[0], q])
    n = len(P)
    for j in range(1, n):
        if D[j-1].inside(P[j]):
            D[j] = D[j-1]
        else:
            D[j] = minidiscwith2points(P[:j], P[j], q, D)
    return D[n-1]

def minidisc(P):
    n = len(P)
    D = [ disc() for i in range(n)]
    D[1] = disc(points=[P[0], P[1]])
    for i in range(2, n):
        if D[i-1].inside(P[i]):
            D[i] = D[i-1]
        else:
            D[i] = minidiscwithpoint(P[:i], P[i], D)
    return D[n-1]

def test():
    n = 5
    points = []
    for i in xrange(n):
        p = Point(random.random(), random.random())
        points.append(p)
    print points
    print minidisc(points)

if __name__ == '__main__':
    test()
