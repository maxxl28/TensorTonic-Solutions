def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    Works for points of any dimension.
    """
    assignments = []
    for point in points:
        current_cluster = 0
        closest_distance = float("inf")
        for c, centroid in enumerate(centroids):
            # squared Euclidean distance in any dimension
            dist = sum((p - q) ** 2 for p, q in zip(point, centroid))
            if dist < closest_distance:
                current_cluster = c
                closest_distance = dist
        assignments.append(current_cluster)
    return assignments
