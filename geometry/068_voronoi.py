import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Define the set of points (sites)
points = np.array([
    [2, 3], [5, 5], [8, 3], [4, 7], [6, 9],
    [1, 8], [9, 7], [3, 1], [7, 2], [9, 9]
])

# Generate the Voronoi diagram
vor = Voronoi(points)

# Plotting the Voronoi diagram
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2, point_size=20)

# Plot the original points
ax.plot(points[:, 0], points[:, 1], 'o', color='red')

# Set plot limits and title
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Voronoi Diagram')

# Display the plot
plt.show()

