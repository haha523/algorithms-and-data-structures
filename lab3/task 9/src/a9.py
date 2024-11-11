import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)

    mid = len(points) // 2
    mid_point = points[mid]

    dl = closest_pair(points[:mid])
    dr = closest_pair(points[mid:])

    d = min(dl, dr)

    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    return min(d, strip_closest(strip, d))

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    points = [tuple(map(int, f.readline().strip().split())) for _ in range(n)]

points.sort(key=lambda point: point[0])

min_distance = closest_pair(points)

with open('output.txt', 'w') as f:
    f.write(f"{min_distance:.4f}\n")