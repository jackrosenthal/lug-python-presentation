def tourlen(tour):
    return sum(dist(a, b) for a, b in zip(tour, tour[1:] + tour[:1]))

def exhaustive(points):
    st = points.pop(0)
    return list(min(((st,) + p for p in permutations(points)), key=tourlen))
