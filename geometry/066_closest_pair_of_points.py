import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest_pair(points):
    """Find the closest pair of points using the brute-force approach."""
    min_dist = float('inf')
    p1 = p2 = None
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                p1, p2 = points[i], points[j]
                
    return p1, p2, min_dist

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    """Recursive function to find the closest pair of points using divide-and-conquer."""
    n = len(points_sorted_by_x)
    
    if n <= 3:
        # If there are 3 or fewer points, use brute force
        return brute_force_closest_pair(points_sorted_by_x)
    
    mid = n // 2
    mid_point = points_sorted_by_x[mid]

    # Divide points into two halves
    left_x = points_sorted_by_x[:mid]
    right_x = points_sorted_by_x[mid:]

    left_y = list(filter(lambda p: p.x <= mid_point.x, points_sorted_by_y))
    right_y = list(filter(lambda p: p.x > mid_point.x, points_sorted_by_y))

    # Recursively find the smallest distance in both halves
    (p1_left, p2_left, min_dist_left) = closest_pair_recursive(left_x, left_y)
    (p1_right, p2_right, min_dist_right) = closest_pair_recursive(right_x, right_y)

    # Find the smaller of the two distances
    if min_dist_left < min_dist_right:
        min_dist = min_dist_left
        closest_pair = (p1_left, p2_left)
    else:
        min_dist = min_dist_right
        closest_pair = (p1_right, p2_right)

    # Check if there exists a closer pair that straddles the divide
    strip = [p for p in points_sorted_by_y if abs(p.x - mid_point.x) < min_dist]
    strip_size = len(strip)
    
    for i in range(strip_size):
        for j in range(i + 1, strip_size):
            if (strip[j].y - strip[i].y) < min_dist:
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (strip[i], strip[j])

    return closest_pair[0], closest_pair[1], min_dist

def closest_pair_of_points(points):
    """Main function to find the closest pair of points using divide-and-conquer."""
    points_sorted_by_x = sorted(points, key=lambda p: p.x)
    points_sorted_by_y = sorted(points, key=lambda p: p.y)
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

# Example usage:
points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]

# Brute-force approach
p1, p2, min_dist = brute_force_closest_pair(points)
print(f"Brute-force: The closest pair of points is {p1} and {p2} with a distance of {min_dist:.4f}")

# Divide and conquer approach
p1, p2, min_dist = closest_pair_of_points(points)
print(f"Divide and Conquer: The closest pair of points is {p1} and {p2} with a distance of {min_dist:.4f}")
