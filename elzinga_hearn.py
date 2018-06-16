from math import pi
import random
from disc import *
import sys
sys.path.append('../geom')
from point import *
from cp import get_angle

def right_obtuse_triangle(p3):
    """
    if true, set p3[0] and p3[1] to define the longest edge
    and p3[2] is on the angle >= 90
    """
    angle0 = get_angle(p3[0], p3[1], p3[2])
    angle1 = get_angle(p3[1], p3[0], p3[2])
    angle2 = pi - angle0 - angle1
    maxa = -1.0
    maxi = -1
    for i, a in enumerate([angle0, angle1, angle2]):
        if a > maxa:
            maxa = a
            maxi = i
    if maxa >= pi/2.0:
        if maxi != 2:
            p3[maxi], p3[2] = p3[2], p3[maxi]
	return True
    return False

def find_three(p3, D, d):
    """
    Given three points in p3, an outside point D, and the
    disc d, find A, C, D and assign them to p3[0], p3[1],
    and p3[2], respectively
    """
    maxd = 0
    for i in range(len(p3)):
        tmpd = p3[i].distance(D)
        if tmpd > maxd:
            maxd = tmpd
            iA = i
    x1 = p3[iA].x
    x2 = d.center.x
    y1 = p3[iA].y
    y2 = d.center.y
    a = y2-y1
    b = -(x2-x1)
    c = (x2-x1)*y1 - (y2-y1)*x1
    eqd = a*D.x + b*D.y + c
    positive = eqd > 0
    eq = [0 for i in range(3)]
    iC = -1
    for i in range(3):
	if i==iA:
	    eq[i] = 0.0
	else:
	    eq[i] = a*p3[i].x + b*p3[i].y + c
	    if positive != ((eq[i]>0)):
		iC = i
    if iC == -1:
	tempf = 100000000.0
	for i in range(3):
	    if i == iA:
		continue;
	    if fabs(eq[i]) < tempf:
		tempf = fabs(eq[i])
		iC = i
    p3[0], p3[1], p3[2] = p3[iA], p3[iC], D
    return

def cover_all(points, d, pp):
    for p in points:
        if p in pp:  # handle precision in float numbers
            continue
        if not d.inside(p):
            return False, p
    return True, None

def onecenter2(P):
    p3 = [Point(-1, -1) for i in range(3)]
    p3[0] = P[0]
    p3[1] = P[1]
    d = disc(points=[p3[0], p3[1]])
    n = len(P)
    cnt = 0
    stop, p3[2] = cover_all(P, d, p3[:2])
    while not stop:
        if right_obtuse_triangle(p3): # right/obtuse triangle
            d = disc(points=[p3[0], p3[1]])
            stop, p3[2] = cover_all(P, d, p3[:2])
        else:                         # strict acute triangle
            d = disc(points=[p3[0], p3[1], p3[2]])
            stop, pd = cover_all(P, d, p3)  # pd outside d
            if not stop:
                find_three(p3, pd, d)
        cnt += 1
    return d

def test():
    npts = 50
    points = []
    for i in xrange(npts):
        p = Point(random.random(), random.random())
        points.append(p)
    print onecenter2(points)

if __name__ == '__main__':
    test()
