import pygal
from die import Die

# Create a D6 die.
die = Die()

# Make some rolls, and store results in a list.
results = []
for i in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency_number = results.count(value)
    frequencies.append(frequency_number)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 1000 times."
hist.x_labels = list(range(1, die.num_sides+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/die_visual.svg')