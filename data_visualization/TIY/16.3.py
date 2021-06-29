import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\hollister_rain_data.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highest_temp, lowest_temp, rain_total = [], [], [], []
    for row in reader:
        dates.append(row[0])
        highest_temp.append(int(row[1]))
        lowest_temp.append(int(row[2]))
        rain_total.append(float(row[3]))

current_date = '12/6/2019'

fig = plt.figure(figsize=(22, 9))
fig.suptitle("Monthly Temperature & Rainfall of 2019", fontsize=24, fontweight="bold")

plt.subplot(2, 1, 1)

plt.title("Hollister, California", fontsize=24)
plt.plot(dates, highest_temp, c="Red", label='Highest Temp.', alpha=0.5)
plt.plot(dates, lowest_temp, c="Blue", label='Lowest Temp.', alpha=0.5)
plt.text(dates[-2], 90, '**Plot made on 12/6/2018**\nData for December is incomplete.', 
        horizontalalignment='center', verticalalignment='center')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(dates, rain_total, c="Blue", label='Rain Total in Inches', alpha=0.5)
plt.legend()

plt.show()