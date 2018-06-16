from elzinga_hearn import *
from welzl import *
from cp import *

import time

n = 50000
points = [ Point(random.random(), random.random())
           for i in range(n) ]

########################################
#
# Test performance using random start
#
########################################

time1 = time.time()
d1 = minidisc(points)
time2 = time.time()
d1t = time2-time1

d2 = onecenter2(points)
time3 = time.time()
d2t = time3-time2

d3 = onecenter1(points)
time4 = time.time()
d3t = time4-time3

print "Welzl           ", d1t, d1
print "Elzinga-Hearn   ", d2t, d2
print "Chrystal-Peirce ", d3t, d3

########################################
#
# Test performance after data preparation
#
########################################

time0 = time.time()
moveminimaxpoints(points)

time1 = time.time()
d1 = minidisc(points)
time2 = time.time()
d1t = time2-time1

d2 = onecenter2(points)
time3 = time.time()
d2t = time3-time2

d3 = onecenter1(points)
time4 = time.time()
d3t = time4-time3

print "Data preparation", time1-time0

print "Welzl           ", d1t, d1
print "Elzinga-Hearn   ", d2t, d2
print "Chrystal-Peirce ", d3t, d3
