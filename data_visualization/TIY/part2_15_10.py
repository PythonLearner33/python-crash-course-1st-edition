import pygal
from part3_15_10 import RandomWalk

# Gameplan: 
# Create a scatterplot and plot the points of a random walk.

# Instantiate a random walk with 1000 steps and call method.
rw = RandomWalk(1000)
walk = rw.fill_walk()

# Instantiate a scatter plot with no stroke or x and y labels.
scatter = pygal.XY(stroke=False, show_x_labels=False, show_y_labels=False)

# Add a title and data to be pointed on graph. 
scatter.title = 'Random Walk'
scatter.add(None, walk)

# Render .svg file.
scatter.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/part2_15_10.svg')