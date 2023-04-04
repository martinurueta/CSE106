import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the file
df = pd.read_csv('weather_data.txt', sep=',')

# convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# a. Actual max temperature and actual min temperature on the same line chart
plt.plot(df["date"], df["actual_max_temp"], color='red', label='Actual Max Temp')
plt.plot(df["date"], df["actual_min_temp"], color='blue', label='Actual Min Temp')
plt.title('Actual Max and Min Temperatures Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.legend()
plt.show()

# b. A histogram of actual precipitation
plt.hist(df["actual_precipitation"], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Actual Precipitation')
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.show()