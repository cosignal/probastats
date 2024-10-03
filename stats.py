"""
Module Name: stats.py
Description: Basic functionality for statistics.
Author: James Hansen
Created: 10/2/24
"""

import math
from copy import deepcopy

def least_to_greatest(list):
    # TODO: opportunity for QUICKSORT refresher
    return

def sample_mean(sample):
    sum = 0
    for x in sample:
        sum += x
    return (sum/len(sample))

def median(sample, sorted=False):
    if (not sorted):
        sample = deepcopy(sample)
        sample.sort() # using this for now (TODO: your own)
    n = len(sample)
    if (n%2 == 0):
        return (sample[int(n/2)]+sample[int((n/2)-1)])/2
    else:
        return sample[int((n/2)-0.5)]

def mode(sample):
    count = 0
    valcounts = {}
    for x in sample:
        try:
            valcounts[x] += 1
        except KeyError:
            valcounts[x] = 1
    
    for val in valcounts:
        if (valcounts[val] > count):
            count = valcounts[val]
            mode = val

    if (count == 1):
        print("No mode")
        return None
    else:
        return mode

def five_number_summary(sample, sorted=False):
    if (not sorted):
        sample = deepcopy(sample)
        sample.sort()
    n = len(sample)
    min = sample[0]
    max = sample[n-1]
    med = median(sample, True)
    if (n%2 == 0):
        q1 = median(sample[0:int(n/2)], True)
        q3 = median(sample[int(n/2):], True)
    else:
        q1 = median(sample[0:int((n/2)-0.5)], True)
        q3 = median(sample[int((n/2)+0.5):], True)
    return [min, q1, med, q3, max]

def outlier_limits(sample, sorted=False):
    if sorted:
        fns = five_number_summary(sample, sorted=True)
    else:
        fns = five_number_summary(sample)

    limits = {}
    iqr = fns[3] - fns[1]
    limits["lower_limit"] = fns[1] - 1.5*iqr
    limits["upper_limit"] = fns[3] + 1.5*iqr
    return limits

def outliers(sample, sorted=False):
    if sorted:
        limits = outlier_limits(sample, sorted=True)
    else:
        limits = outlier_limits(sample)
    
    outliers = {"lower": [], "upper": []}
    for x in sample:
        if (x < limits["lower_limit"]):
            outliers["lower"].append(x)
        elif (x > limits["upper_limit"]):
            outliers["upper"].append(x)
    if (len(outliers["lower"])==0 and len(outliers["upper"])==0):
        print("No outliers")
        return None
    else:
        return outliers

def adjacent_points(sample, sorted=False):
    # outliers taken to be sorted given order of appendation in outliers()
    if sorted:
        o = outliers(sample, sorted=True)
    else:
        o = outliers(sample)
    
    if (o is None):
        return {"min": sample[0], "max": sample[len(sample)-1]}

    adjacent_points = {}
    for idx in range(len(sample)):
        if (sample[idx] == o["lower"][len(o["lower"])-1]):
            min_idx = idx+1
            adjacent_points["min"] = sample[min_idx]
            break
    for idx in range(min_idx, len(sample)):
        if (sample[idx] == o["upper"][0]):
            adjacent_points["max"] = sample[idx-1]
    return adjacent_points

def population_standard_deviation(population):
    sum = 0
    mean = sample_mean(population)
    for x in population:
        sum += (x-mean)*(x-mean)
    return math.sqrt(sum/len(population))

def sample_standard_deviation(sample):
    sum = 0
    mean = sample_mean(sample)
    for x in sample:
        sum += (x-mean)*(x-mean)
    return math.sqrt(sum/(len(sample)-1))
    