import matplotlib.pyplot as plt
from dice15_10 import Die

# Game Plan:
#   Visualize 1000 dice rolls with two D6s.

# Instantiate Dice.
die_1 = Die()
die_2 = Die()

# Calculate data from rolling dice.
results = [die_1.roll() + die_2.roll() for i in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequency = [results.count(i) for i in range(1, max_result+1)]

# Create histogram.
plt.hist(results, rwidth=0.99)

plt.title("Frequency of Dice Results", fontsize=13)
plt.xlabel("Dice Number", fontsize=13)
plt.ylabel("Frequency", fontsize=13)

plt.axis([2, 12, 0, 200])

plt.show()