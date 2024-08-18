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

def jarvis_march(points):
    """Compute the convex hull using Jarvis's March algorithm."""
    n = len(points)
    if n < 3:
        return []  # Convex hull is not possible with fewer than 3 points

    # Initialize result list for the convex hull points
    hull = []

    # Find the leftmost point
    leftmost = min(points, key=lambda p: p.x)
    p = leftmost

    while True:
        # Add current point to hull
        hull.append(p)

        # Select the next point in the convex hull
        q = points[0]
        for r in points:
            if orientation(p, q, r) == 2 or (q == p):
                q = r
        
        p = q

        # Check if we have returned to the first hull point
        if p == leftmost:
            break

    return hull

# Example usage:
points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), 
          Point(3, 0), Point(0, 0), Point(3, 3)]
hull = jarvis_march(points)
print("The points in the Convex Hull are:")
for p in hull:
    print(p)
