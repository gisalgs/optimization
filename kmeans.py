"""
k-means

History
    November 29, 2016
        import geom.point
        comments added

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

from random import random, sample, uniform
from math import fabs, sqrt

import os, sys
lib_path = os.path.abspath('../')
sys.path.insert(0, lib_path)
from geom.point import *

INF = float('inf')

def clustering_dist(points, means):
    """
    Computing distances for the k-means

    Input
      points:    list of Point objects
      means:     list of k points that serve as the means

    Output
      nearests:  list of lists, where each inner list holds the id of nearest points to each mean
      totaldist: average distances between each point to its nearest mean
    """
    n = len(points)
    k = len(means)
    nearests = [[] for i in range(k)]
    totaldist = 0
    for i in range(n):
        dmin = INF
        near = []
        for j in range(k):
            d = points[i].distance(means[j])
            if d < dmin:
                dmin = d
                jmin = j
        totaldist += dmin
        nearests[jmin].append(i)
    totaldist = totaldist/n
    return nearests, totaldist

def initk(points, k, init):
    """
    Initialization for k-means

    Input
      points:    list of Point objects
      k:         integer
      init:      initialization method ('forgy' or 'random')

    Output
      means:     list of k Point objects
      nearests:  list of lists, where each inner list holds the id of nearest points to each mean
      totaldist: average distances between each point to its nearest mean
    """
    n = len(points)
    xmin = INF
    ymin = INF
    xmax = -INF
    ymax = -INF
    for p in points:
        xmin = min([xmin, p.x])
        ymin = min([ymin, p.y])
        xmax = max([xmax, p.x])
        ymax = max([ymax, p.y])
    nearests = [[] for i in range(k)]
    while [] in nearests: # until not empty sets in nearests
        if init=="forgy":   # Forgy initialization
            means = [points[i] for i in sample(range(n), k)]
        elif init=="random":
            means = [ Point(uniform(xmin, xmax), uniform(ymin, ymax)) for i in range(k) ]
        else:
            print "Error: unknown initialization method"
            sys.exit(1)
        nearests, totaldist = clustering_dist(points, means)
    return means, nearests, totaldist

def kmeans(points, k, threshold=1e-5, init="forgy", verbose=False):
    """
    Input
      points:     list of Point objects
      k:          integer, the number of means
      threshould: minimal improvement between iterations
      init:       initialization method ('forgy' or 'random')

    Output
      means:      list of k Point objects
      totaldist:  average distances between each point to its nearest mean
    """
    bigdiff = True
    means, nearests, totaldist = initk(points, k, init)
    if verbose:
        print means
    while bigdiff:
        means2 = []
        for j in range(k):
            cluster = [xx for xx in nearests[j]]
            sumx = sum([points[ii].x for ii in cluster])
            sumy = sum([points[ii].y for ii in cluster])
            numpts = len(nearests[j])
            if numpts>0:
                sumx = sumx/numpts
                sumy = sumy/numpts
            means2.append(Point(sumx, sumy))
        nearests, newtotal = clustering_dist(points, means2)
        offset = totaldist - newtotal
        if offset > threshold:
            means = means2
            totaldist = newtotal
            if verbose:
                print means
        else:
            bigdiff = False
    return totaldist, means

def test():
    n = 5000
    points = [ Point(random(), random()) for i in range(n) ]

    print kmeans(points, 10, init="forgy")[0]

    points1 = [ Point(uniform(10, 20), uniform(10, 20)) for i in range(n/2) ]
    points2 = [ Point(uniform(30, 40), uniform(30, 40)) for i in range(n/2) ]

    print kmeans(points1+points2, 2)[0]

    points1 = [ Point(uniform(10, 20), uniform(10, 20)) for i in range(n/3) ]
    points2 = [ Point(uniform(30, 40), uniform(10, 20)) for i in range(n/3) ]
    points3 = [ Point(uniform(20, 30), uniform(30, 40)) for i in range(n/3) ]

    print kmeans(points1+points2+points3, 3)[0]
    print kmeans(points1+points2+points3, 3, init="random")[0]

if __name__ == "__main__":
    test()
