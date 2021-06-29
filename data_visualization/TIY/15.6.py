import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for i in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()
hist.title, hist.x_title, hist.y_title = "Results of rolling two D6 1000 times.", "Result", "Frequency of Result"
hist.x_labels = list(range(2, max_result+1))
hist.add('D6 + D6', frequencies)
hist.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/15_6.svg')