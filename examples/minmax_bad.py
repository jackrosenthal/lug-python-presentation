min_dist = float('inf')
for p in points:
    d = dist(p, z)
    if d < min_dist:
        x = p
