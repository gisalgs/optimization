import random
import sys
sys.path.append('..')
from optimization.disc import *
from geom.point import *

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

def minidisc(P, verbose=False):
    n = len(P)
    D = [ disc() for i in range(n)]
    D[1] = disc(points=[P[0], P[1]])
    for i in range(2, n):
        if verbose:
            very_simple_progress_bar(i, n)
        if D[i-1].inside(P[i]):
            D[i] = D[i-1]
        else:
            D[i] = minidiscwithpoint(P[:i], P[i], D)
    return D[n-1]


def very_simple_progress_bar(current, upper, size=20):
    '''
    current    an integer indicating the current step
    upper      an integer indicating the number of iterations
    size       the length of the progress bar
    
    we assume the lower end is zero.
    '''
    barx = int(size*(current+1)/upper)
    print('\r[{}{}] {}/{}'.format('x'*barx, '-'*(size-barx), current+1, upper), end='', flush=True)

def test(n=5):
    points = [Point(random.random(), random.random()) for _ in range(n)]
    print(points)
    res = minidisc(points, True)
    print(res)

if __name__ == '__main__':
    test()

