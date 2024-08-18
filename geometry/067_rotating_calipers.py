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

def convex_hull(points):
    """Compute the convex hull of a set of 2D points using Graham's scan algorithm."""
    points = sorted(points, key=lambda p: (p.x, p.y))
    
    def cross(o, a, b):
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def rotating_calipers(points):
    """Find the diameter of a convex polygon using rotating calipers."""
    n = len(points)
    if n == 1:
        return 0
    elif n == 2:
        return distance(points[0], points[1])

    k = 1
    max_dist = 0

    for i in range(n):
        while True:
            # Calculate distance between point i and k
            current_dist = distance(points[i], points[k])
            next_k = (k + 1) % n
            next_dist = distance(points[i], points[next_k])
            
            # Update k if the next distance is greater
            if next_dist > current_dist:
                k = next_k
            else:
                break
        
        # Update max_dist if a larger distance is found
        max_dist = max(max_dist, distance(points[i], points[k]))

    return max_dist

# Example usage:
points = [
    Point(0, 3), Point(1, 1), Point(2, 2),
    Point(4, 4), Point(0, 0), Point(1, 2),
    Point(3, 1), Point(3, 3)
]

# Step 1: Compute the convex hull
convex_hull_points = convex_hull(points)
print(f"Convex Hull Points: {convex_hull_points}")

# Step 2: Compute the diameter using rotating calipers
diameter = rotating_calipers(convex_hull_points)
print(f"Diameter of the convex polygon: {diameter:.4f}")
