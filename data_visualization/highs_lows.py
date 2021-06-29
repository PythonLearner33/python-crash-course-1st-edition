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
filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f) # Reader object; to be used by Python, reads line-by-line.
    header_row = next(reader) # Skips over header row (first row) once "next()" is declared.

    # IMPORTANT: List-comprehesions do not work to my knowledge as of currently because
    #            apparantly you cannot call the reader object twice.
    #            lotta buggy shit here in the for row loop. datetime.strftime especially
    #            i think date time converts or sections off pieces of data like the month and days
    #            bins is what i mean. removing datetime.strptime makes every date show up. maybe
    #            matplotlib does some converting for you.

    dates, highs, lows = [], [], []
    
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print("Incomplete Data", row)
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(figsize=(22, 9))
plt.plot(dates, highs, c="Red", alpha=0.5)
plt.plot(dates, lows, c="Blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="Blue", alpha=0.1)

# Format plot.
plt.title("Daily High and Low Temperatures - 2014\nDeath Valley", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() # (1)Idk what this logically says, book just told me to put it. might check later idk.
                    # (1)turns dates diagonally so no overlapping dates.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()