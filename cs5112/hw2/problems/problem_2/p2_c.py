'''
Problem 2c
'''

import math
from collections import defaultdict
import random

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def cell_key(pt, cell_size):
    return (int(pt[0] / cell_size), int(pt[1] / cell_size))

def closest_pair(points):
    n = len(points)

    # Order the points in a random sequence
    random.shuffle(points)

    best_pair = points[0], points[1]
    # Let delta denote the minimum distance found so far
    delta = d(best_pair[0], best_pair[1])

    # Invoke MakeDictionary for storing subsquares of side length delta/2
    cell_size = delta / 2.0
    dictionary = defaultdict(list)
    
    # Add first two points to dictionary
    dictionary[cell_key(points[0], cell_size)].append(points[0])
    dictionary[cell_key(points[1], cell_size)].append(points[1])

    nearest_9_offsets = [(di, dj) for di in range(-1, 2) for dj in range(-1, 2)]

    for i in range(2, n):
        pi = points[i]
        key_i = cell_key(pi, cell_size)

        # Look up the subsquares close to pi
        best_local_delta = delta
        best_local_pair = best_pair
        for di, dj in nearest_9_offsets:
            subsquare_key = (key_i[0] + di, key_i[1] + dj)
            if subsquare_key in dictionary:
                for pj in dictionary[subsquare_key]:
                    # Compute the distance from pi to any points found in these subsquares
                    dist = d(pi, pj)
                    if dist < best_local_delta:
                        best_local_delta = dist
                        best_local_pair = (pi, pj)
     
        if best_local_delta < delta:
            # Found improvement, rebuild dictionary
            delta = best_local_delta
            best_pair = best_local_pair
            cell_size = delta / 2.0
            dictionary = defaultdict(list)
            for j in range(i + 1):
                pt = points[j]
                key = cell_key(pt, cell_size)
                dictionary[key].append(pt)
        else:
            # Insert pi into the current dictionary
            dictionary[key_i].append(pi)

    return best_pair