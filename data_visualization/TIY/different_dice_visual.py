import pygal
from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for i in range(50000):
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

hist.title = "Results of rolling a D6 and D10 50,000 times."
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/different_dice_visual.svg')