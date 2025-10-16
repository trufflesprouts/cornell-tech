'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    n = len(points)
    
    # sort points by x-axis
    points.sort()

    best_pair = (None, None)
    min_dist = float("inf")

    def update_answer(p1, p2):
        nonlocal best_pair
        nonlocal min_dist
        dist = d(p1, p2)
        if dist < min_dist:
            min_dist = dist
            best_pair = (p1, p2)
    
    def merge_by_y(l, m, r):
        temp = [None] * (r - l)
        i, j, k = l, m, 0
        while i < m and j < r:
            if points[i][1] <= points[j][1]:
                temp[k] = points[i]
                i += 1
            else:
                temp[k] = points[j]
                j += 1
            k += 1
        while i < m:
            temp[k] = points[i]
            i += 1
            k += 1
        while j < r:
            temp[k] = points[j]
            j += 1
            k += 1
        points[l:r] = temp
    
    def rec(l, r):
        if r - l <= 3:
            # Base case: brute force for small subarrays
            for i in range(l, r):
                for j in range(i + 1, r):
                    update_answer(points[i], points[j])
            # sort strip by y-axis
            points[l:r] = sorted(points[l:r], key=lambda p: p[1])
            return
        
        # find median
        m = (l + r) >> 1
        mid_x = points[m][0]
        
        # recurse on both sides
        rec(l, m)
        rec(m, r)
        
        # combine (this is tricky)
        merge_by_y(l, m, r)
        
        # check points in the strip
        strip = []
        for i in range(l, r):
            if abs(points[i][0] - mid_x) < min_dist:
                # compare each to next 11
                start = max(0, len(strip) - 11)
                for j in range(start, len(strip)):
                    if points[i][1] - strip[j][1] < min_dist:
                        update_answer(points[i], strip[j])
                strip.append(points[i])

    rec(0, n)
    
    return best_pair

