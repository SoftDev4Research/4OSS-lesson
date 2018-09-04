from sys import *
import os, numpy

def lowhigh(numarray):
    try:
        ordered_positives = numpy.array(filter(lambda x: x > 0, sorted(numarray)))
    except TypeError:
        raise TypeError("You must provide an array of numeric objects to lowhigh. Please check your input.")
    high=ordered_positives [-1]
    low=ordered_positives [0]
    return (high, low)

i = argv[1]
with open(i, 'r') as ifh:
    for line in ifh.readlines():
        n = numpy.array(line.strip().split(), dtype=float)
        print("high: {1}; low: {0}".format(lowhigh(n)))
