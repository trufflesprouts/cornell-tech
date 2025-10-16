'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''
def stable_matching_1c(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    # doctors_rank[d][h] = rank of hospital h in doctor d's preference list
    doctors_rank = [[0] * n for _ in range(n)]
    for d in range(n):
        for rank, h in enumerate(doctors_pref[d]):
            doctors_rank[d][h] = rank
    
    # doctors to hospitals map
    pairs = {} 
    matched_hospitals = set()

    while len(matched_hospitals) < n:
        for h in range(n):
            if h not in matched_hospitals:
                doc_preference = hospitals_pref[h].pop(0)

                # If the hospital's preference hasn't been matched
                if doc_preference not in pairs:
                    pairs[doc_preference] = h
                    matched_hospitals.add(h)

                # If the hospital's preference already has a match
                else:
                    h2 = pairs[doc_preference]
                    # Use precomputed rankings for O(1) comparison
                    if doctors_rank[doc_preference][h] < doctors_rank[doc_preference][h2]:
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs