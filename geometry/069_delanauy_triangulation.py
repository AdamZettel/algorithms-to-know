import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Define a set of points
points = np.array([
    [2, 3], [5, 5], [8, 3], [4, 7], [6, 9],
    [1, 8], [9, 7], [3, 1], [7, 2], [9, 9]
])

# Compute the Delaunay triangulation
tri = Delaunay(points)

# Plot the points
plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'o', color='red', markersize=8, label='Points')

# Plot the Delaunay triangulation
for simplex in tri.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'b-', lw=1.5)

# Set plot limits and title
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Delaunay Triangulation')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Display the plot
plt.show()
