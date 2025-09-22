import os

'''
Problem 1
Funciton to verify the output is a stable matching.
'''
def verify_output(file, pairs) -> bool:
    n = 0
    doctors_pref = {}
    hospitals_pref = {}

    reverse_pairs = {}
    for x in pairs:
        reverse_pairs[pairs[x]] = x

    with open(file, "r") as f:
        n = int(f.readline())
        assert n == len(pairs)

        for i in range(n):
            doctors_pref[i] = {}
            d_pref = f.readline().split()
            for j in range(len(d_pref)):
                doctors_pref[i][int(d_pref[j])] = j

        for i in range(n):
            hospitals_pref[i] = {}
            h_pref = f.readline().split()
            for j in range(len(h_pref)):
                hospitals_pref[i][int(h_pref[j])] = j

    for doc in pairs:
        for x in range(n):
            # if doc would have prefered this case
            if doctors_pref[doc][pairs[doc]] > doctors_pref[doc][x]:
                # If the hospital would also prefer this case
                if hospitals_pref[x][doc] <  hospitals_pref[x][reverse_pairs[x]]:
                    return False
    
    return True

'''
Problem 1
Broken implementation from problem 1a
'''
def stable_matching_1a(file) -> dict:
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
                    h1_idx = doctors_pref[doc_preference].index(h)
                    h2_idx = doctors_pref[doc_preference].index(h2)
                    if h1_idx > h2_idx:
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs

'''
Problem 1
Funciton to verify the txt files where students need to include
test cases.
'''
def verify_formating(file, expected_n=None):
    is_empty = os.path.getsize(file)
    if (is_empty == 0):
        print("The file is empty.")
        return False

    with open(file, "r") as f:
        n = f.readline()
        # In case there is an accidental new line at the begining of the file
        while n.strip() == "":
            n = f.readline()

        try:
            n = int(n)
            assert n < 100
            if expected_n is not None:
                assert expected_n == n

            for _ in range(2*n):
                line = f.readline()
                line_list = line.split()
                assert n == len(line_list)
                for x in line_list:
                    int(x)

            for x in f:
                if x.strip():
                    assert False
            
            return True
        except:
            return False


'''
Problem 2
Function to check the interval cover covers all
the elements in [0, M].
'''
def verify_all_is_covered(M, cover) -> bool:
    cover = sorted(cover, key=lambda x: x[0])
    interval = cover[0]
    for pair in cover[1:]:
        if pair[0] <= interval[0] or pair[0] > interval[1] or pair[1] <= interval[1]:
            return False
        interval[1] = pair[1]
    
    return interval == [0, M]
