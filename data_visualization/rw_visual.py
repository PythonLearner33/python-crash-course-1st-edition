from random_walk import RandomWalk
import matplotlib.pyplot as plt

#while True:
    # Make a random walk, and plot the points.
rw = RandomWalk(50000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(dpi=128, figsize=(22, 11.5))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Red', edgecolors='none', s=100)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

    #continue_map = input("Do you want to draw another RandomWalk? y/n: ")
    #if continue_map.lower() == 'n':
        #break