import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=14)
plt.tick_params(axis='both', labelsize=13)
plt.axis([0, 6, 0, 150])
plt.show()