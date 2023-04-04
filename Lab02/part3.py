import pandas as pd

# Read the data from the file
df = pd.read_csv('weather_data.txt', sep=',')

# a. What day(s) had the highest actual precipitation?
print("Part a")

df.sort_values(by=['actual_precipitation'], inplace=True, ascending=False)
print(df.head())

# b. What was the average actual max temp for July 2014?
print("Part b")
df_july2014 = df.loc[df['date'].str.contains('2014-7')]
avg_max_temp = df_july2014['actual_max_temp'].mean()
print(avg_max_temp, 'degrees')


# c. What days was the actual max temp the record max temp?
print("Part c")

actual_max_temp_is_record_max_temp = df.loc[df['actual_max_temp'] == df['record_max_temp']]
print(actual_max_temp_is_record_max_temp.head())

# d. How much did it rain in October 2014?
print("Part d")

totalRain = df.loc[df['date'].str.contains('2014-10')]['actual_precipitation'].sum()
print(totalRain)

# e. What day(s), if any, was the actual low temperature below 60 degrees and actual max temperature above 90 degrees on the same day?
print("Part e")
below60_and_above_90 = df.loc[(df['actual_min_temp'] < 60) & (df['actual_max_temp'] > 90)]
if below60_and_above_90.empty:
    print("No days found")
