import csv
import matplotlib.pyplot as plt
from datetime import datetime

# --------
# Gameplan:
# --------
#   - Sort dates and high and low temperatures from .csv file.
#   - Plot dates and high and low temperatures.
# --------

# Sort data.
filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\death_valley_2014.csv'
filename2 = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f) # Reader object; to be used by Python, reads line-by-line.
    header_row = next(reader) # Skips over header row (first row) once "next()" is declared.

    dates_d, highs_d, lows_d = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print("Incomplete Data", row)
        else:
            dates_d.append(current_date)
            highs_d.append(high)
            lows_d.append(low)

with open(filename2) as f:
    reader = csv.reader(f) # Reader object; to be used by Python, reads line-by-line.
    header_row = next(reader) # Skips over header row (first row) once "next()" is declared.

    dates_s, highs_s, lows_s = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print("Incomplete Data", row)
        else:
            dates_s.append(current_date)
            highs_s.append(high)
            lows_s.append(low)

# Plot data.

# Death Valley, California
fig = plt.figure(figsize=(22, 9))
plt.suptitle("Daily High and Low Temperatures - 2014", fontsize=24, fontweight='bold')
plt.subplot(2, 1, 1)
plt.plot(dates_d, highs_d, c="Red", alpha=0.5)
plt.plot(dates_d, lows_d, c="Blue", alpha=0.5)
plt.fill_between(dates_d, highs_d, lows_d, facecolor="Blue", alpha=0.1)
plt.title("Death Valley", fontsize=25)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Sitka, Alaska
plt.subplot(2, 1, 2)
plt.plot(dates_s, highs_s, c="Red", alpha=0.5)
plt.plot(dates_s, lows_s, c="Blue", alpha=0.5)

plt.fill_between(dates_s, highs_s, lows_s, facecolor="Blue", alpha=0.1)

fig.autofmt_xdate()

plt.title("Sitka", fontsize=25)
plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()