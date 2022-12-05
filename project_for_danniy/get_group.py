def name_gr(popularity):
    groups = {1: (100000, 10**10),
            2: (30000, 100000),
            3: (10000, 30000),
            4: (5000, 10000),
            5: (0, 5000)}
    for i in range(1, len(groups)+1):
        lower, upper = groups[i]
        if lower <= popularity < upper:
            return i

def fam_gr(popularity):
    groups = {1: (40000, 10**10),
            2: (20000, 40000),
            3: (10000, 20000),
            4: (5000, 10000),
            5: (0, 5000)}
    for i in range(1, len(groups)+1):
        lower, upper = groups[i]
        if lower <= popularity < upper:
            return i

def otch_gr(popularity):
    groups = {1: (1000000, 10**10),
            2: (100000, 1000000),
            3: (10000, 100000),
            4: (5000, 10000),
            5: (0, 5000)}
    for i in range(1, len(groups)+1):
        lower, upper = groups[i]
        if lower <= popularity < upper:
            return i
