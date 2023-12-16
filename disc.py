from math import fabs, sqrt
import sys

sys.path.append('..')
from geom.point import *

__all__ = ['disc']

class disc:
    def __init__(self, center=None, radius=None, points=None):
        if points == None:
            self.center = center
            self.radius = radius
        else:
            if len(points)==2:
                res = make_disc2(points[0],points[1])
            elif len(points)==3:
                res = make_disc(points[0],points[1],points[2])
            else:
                res = [None, None]
            self.center = res[0]
            self.radius = res[1]
    def __eq__(self, other):
        return self.center==other.center and\
            self.radius==other.radius
    def __repr__(self):
            return "({0}, {1})".format(
                self.center, self.radius)
    def inside(self, p):
        dx = fabs(self.center.x - p.x)
        dy = fabs(self.center.y - p.y)
        if dx>self.radius or dy>self.radius:
            return False
        if self.center.distance(p) <= self.radius:
            return True
        return False

def make_disc2(p1, p2):
    dx = fabs(p1.x - p2.x)
    dy = fabs(p1.y - p2.y)
    radius = sqrt(dx*dx + dy*dy)/2.0
    x = min(p1.x, p2.x) + dx/2.0
    y = min(p1.y, p2.y) + dy/2.0
    return Point(x, y), radius

def make_disc(p1, p2, p3):
    x1, x2, x3 = p1.x, p2.x, p3.x
    y1, y2, y3 = p1.y, p2.y, p3.y
    a = fabs(x2-x1)
    b = fabs(x3-x1)
    c = fabs((y2-y1)/a - (y3-y1)/b)
    xs = a
    if b < xs:
        xs = b
    if c < xs:
        xs = c
    a = fabs(y2-y1)
    b = fabs(y3-y1)
    c = fabs((x2-x1)/a - (x3-x1)/b)
    ys = a
    if b < ys:
        ys = b
    if c < ys:
        ys = c
    if xs < ys:   # eliminate x, compute y first
    	return make_disc_x(p1, p2, p3)
    else:
	    return make_disc_y(p1, p2, p3)

def make_disc_y(p1, p2, p3):
    x1 = p1.x
    x2 = p2.x
    x3 = p3.x
    y1 = p1.y
    y2 = p2.y
    y3 = p3.y
    t1 = (x1*x1-x3*x3+y1*y1-y3*y3)/(2*(x3-x1))
    t2 = (x1*x1-x2*x2+y1*y1-y2*y2)/(2*(x2-x1))
    t3 = (y2-y1)/(x2-x1) - (y3-y1)/(x3-x1)
    y = (t1 - t2)/t3
    x = -(2*(y2-y1)*y + x1*x1 - x2*x2 + y1*y1 -
          y2*y2) / (2*(x2-x1))
    r = sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))
    return Point(x, y), r

def make_disc_x(p1, p2, p3):
    x1, x2, x3 = p1.x, p2.x, p3.x
    y1, y2, y3 = p1.y, p2.y, p3.y
    t1 = (x1*x1-x3*x3+y1*y1-y3*y3)/(2*(y3-y1))
    t2 = (x1*x1-x2*x2+y1*y1-y2*y2)/(2*(y2-y1))
    t3 = (x2-x1)/(y2-y1) - (x3-x1)/(y3-y1)
    x = (t1 - t2)/t3
    y = -(2*(x2-x1)*x + x1*x1 - x2*x2 + y1*y1 -
          y2*y2) / (2*(y2-y1))
    r = sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))
    return Point(x, y), r
