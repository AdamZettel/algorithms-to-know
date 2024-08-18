from functools import cmp_to_key

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def orientation(p, q, r):
    """Return the orientation of the triplet (p, q, r).
    0 -> p, q and r are collinear
    1 -> Clockwise
    2 -> Counterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def distance_sq(p1, p2):
    """Return the squared Euclidean distance between p1 and p2."""
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def convex_hull(points):
    """Compute the convex hull of a set of 2D points."""
    n = len(points)
    if n < 3:
        return []

    # Step 1: Find the point with the lowest y-coordinate
    min_y = min(points, key=lambda p: (p.y, p.x))
    points.remove(min_y)

    # Step 2: Sort the points by polar angle with the pivot (min_y)
    def compare(p1, p2):
        o = orientation(min_y, p1, p2)
        if o == 0:
            return distance_sq(min_y, p1) - distance_sq(min_y, p2)
        return -1 if o == 2 else 1

    points = sorted(points, key=cmp_to_key(compare))

    # Step 3: Build the convex hull
    hull = [min_y]
    for point in points:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], point) != 2:
            hull.pop()
        hull.append(point)

    return hull

# Example usage:
points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), 
          Point(3, 0), Point(0, 0), Point(3, 3)]
hull = convex_hull(points)
print("The points in the Convex Hull are:")
for p in hull:
    print(p)
