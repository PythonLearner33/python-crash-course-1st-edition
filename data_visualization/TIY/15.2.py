import matplotlib.pyplot as plt

# Commented-out code is part one of TIY.
#x_values = [1, 2, 3, 4, 5]
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, edgecolors='none', s=14)
plt.tick_params(axis='both', labelsize=13)
#plt.axis([0, 6, 0, 150])
plt.axis([0, 5000, 0, 125500000000])
plt.show()