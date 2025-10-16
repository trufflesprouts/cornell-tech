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

    # # Order the points in a random sequence 
    # random.shuffle(points)

    # Let delta denote the minimum distance found so far
    best_pair = points[0], points[1]
    # Initialize delta with p1 and p2
    delta = d(best_pair[0], best_pair[1])

    # Invoke MakeDictionary for storing subsquares of side length delta/2
    cell_size = delta / 2.0
    dictionary = defaultdict(list)
    processed = []

    # Seed dictionary with first two points
    for pt in best_pair:
        processed.append(pt)
        key = cell_key(pt, cell_size)
        dictionary[key].append(pt)

    nearest_25_offsets = [(di, dj) for di in range(-2, 3) for dj in range(-2, 3)]

    for i in range(2, n):
        pi = points[i]

        key_i = cell_key(pi, cell_size)

        # Look up the 25 subsquares close to pi
        best_local_delta = delta
        best_local_pair = best_pair
        candidates = []
        for di, dj in nearest_25_offsets:
            subsquare_key = (key_i[0] + di, key_i[1] + dj)
            if subsquare_key in dictionary:
                candidates.extend(dictionary[subsquare_key])

        # Compute the distance from pi to any points found in these subsquares
        for pj in candidates:
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
            for pt in processed + [pi]:
                key = cell_key(pt, cell_size)
                dictionary[key].append(pt)
            processed.append(pi)
        else:
            # Insert pi into the current dictionary
            dictionary[key_i].append(pi)
            processed.append(pi)

    return best_pair
