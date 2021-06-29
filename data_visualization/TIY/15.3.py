from random_walk import RandomWalk
import matplotlib.pyplot as plt

#while True:
    # Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(dpi=128, figsize=(22, 11.5))

plt.plot(rw.x_values, rw.y_values, linewidth=1)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

    #continue_map = input("Do you want to draw another RandomWalk? y/n: ")
    #if continue_map.lower() == 'n':
        #break