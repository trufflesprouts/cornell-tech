'''
Problem 2a
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    best_pair = (None, None)
    min_dist = float("inf")
    for point in points:
        for other_point in points:
            if point == other_point:
                continue
            dist = d(point, other_point)
            if dist < min_dist:
                min_dist = dist
                best_pair = (point, other_point)
    return best_pair
