class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def distance(p1, p2, p):
    """Calculate the distance of point p from the line p1p2."""
    return abs((p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x))

def on_left(p1, p2, p):
    """Check if point p is on the left of line p1p2."""
    return (p2.x - p1.x) * (p.y - p1.y) - (p2.y - p1.y) * (p.x - p1.x) > 0

def quick_hull(points):
    """Compute the convex hull using the QuickHull algorithm."""
    if len(points) < 3:
        return points

    # Find the leftmost and rightmost points
    min_point = min(points, key=lambda p: p.x)
    max_point = max(points, key=lambda p: p.x)

    # Points that form the convex hull
    convex_hull = []

    def find_hull(subset, p1, p2):
        if not subset:
            return

        # Find the point in subset farthest from the line p1p2
        farthest_point = max(subset, key=lambda p: distance(p1, p2, p))
        convex_hull.append(farthest_point)

        # Partition the subset into two parts
        subset1 = [p for p in subset if on_left(p1, farthest_point, p)]
        subset2 = [p for p in subset if on_left(farthest_point, p2, p)]

        # Recursively find convex hull on both subsets
        find_hull(subset1, p1, farthest_point)
        find_hull(subset2, farthest_point, p2)

    # Initial split: find points on the left and right of the line formed by min_point and max_point
    left_subset = [p for p in points if on_left(min_point, max_point, p)]
    right_subset = [p for p in points if on_left(max_point, min_point, p)]

    # Add the extreme points to the convex hull
    convex_hull.append(min_point)
    convex_hull.append(max_point)

    # Recursively find the convex hull for both subsets
    find_hull(left_subset, min_point, max_point)
    find_hull(right_subset, max_point, min_point)

    return convex_hull

# Example usage:
points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), 
          Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
hull = quick_hull(points)
print("The points in the Convex Hull are:")
for p in hull:
    print(p)
