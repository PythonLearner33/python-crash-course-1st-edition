import pygal
from die import Die
import os

# Create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
roll_number = 100000000

results = []
for i in range(roll_number):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency_number = results.count(value)
    frequencies.append(frequency_number)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8s " + "{:,}".format(roll_number) + " times."
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8 + D8', frequencies)

# Get filename of module.
filepath = __file__
filename = os.path.basename(filepath)

# Render data to .svg file.
hist.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/' + filename + '.svg')