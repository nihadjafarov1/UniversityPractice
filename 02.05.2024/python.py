def calculate_distance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

points = [(23, 15), (13, 22), (16, 17), (30, 30)]

centroid = (sum(x for x, _ in points) / len(points), sum(y for _, y in points) / len(points))

min_total_distance = float('inf')

total_distance = sum(calculate_distance(centroid, point) for point in points)

print("Optimal coordinate (centroid):", centroid)
