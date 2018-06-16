from math import sqrt, atan2, fabs, pi
from disc import *
import sys
sys.path.append('../geom')
from point import *
import random

def get_angle(p0, p1, p2):
    """
    Returns angle between line p0p1 and p0p2 (using
    directions: p0 -> p1, p0 -> p2)
    """
    a1 = atan2(p1.y-p0.y, p1.x-p0.x)
    a2 = atan2(p2.y-p0.y, p2.x-p0.x)
    if a1 < 0: 
	a1 = 2*pi - fabs(a1)
    if a2 < 0: 
	a2 = 2*pi - fabs(a2)
    degree = fabs(a1-a2)
    if degree > pi:
	degree = 2*pi - degree;
    return degree;

def find_mini_angle(S1, A, B, um):
    n = len(S1)
    angle = 100
    c = -1
    for i in xrange(n):
        if S1[i] == A or S1[i] == B:
            continue
        if not um[i]:
            continue
        angle1 = get_angle(S1[i], A, B)
        if angle1 < angle:
            angle = angle1
            c = i #D = S1[i]
        if angle1 < pi/2.0:
            continue
        um[i] = 0
    return angle, c

def getfirsttwo(S):
    b = Point(0, 0)
    dist = 0
    ix = 0
    for i, p in enumerate(S): #  farthest point from origin
        d1 = p.distance(b)
        if d1 > dist:
            dist = d1
            ix = i
            a = p
    dist = 0
    dd = sqrt(a.x*a.x+a.y*a.y)
    for i, p in enumerate(S):
        if i==ix: continue
	d1 = (a.x-p.x)*(a.x-p.x) + (a.y-p.y)*(a.y-p.y)
	d1 = d1*dd / fabs(a.x*(a.x-p.x) + a.y*(a.y-p.y))
	if d1 > dist:
	    dist = d1
	    b = p
	    iy = i
    return ix, iy

def moveminimaxpoints(points):
    mini, maxi = getfirsttwo(points)
    # set minx to 0, maxx to 1
    if maxi != 0:
        points[0],points[mini] = points[mini], points[0]
    if mini != 1:
        points[1],points[maxi] = points[maxi], points[1]

def onecenter1(P):
    n = len(P)
    unmarked = [1 for i in range(n)]
    done = False
    a = 0
    b = 1
    while not done:
        A, B = P[a], P[b]
        angle, c = find_mini_angle(P, A, B, unmarked)
        C = P[c]
        if angle > pi/2.0:
            done = True
            d = disc(points=[A, B])
        elif get_angle(B, A, C) < pi/2.0 and\
        get_angle(A, B, C) < pi/2.0:
            done = True
            d = disc(points=[A, B, C])
        else:
            if (get_angle(B, A, C)) > pi/2.0:
                unmarked[b] = 0
                b = c
            else:
                unmarked[a] = 0
                a = c
    return d

def test():
    npts = 5
    points = []
    for i in xrange(npts):
        p = Point(random.random(), random.random())
        points.append(p)
    print points
    print onecenter1(points)
    moveminimaxpoints(points)
    print points
    print onecenter1(points)
    
if __name__ == '__main__':
    test()
