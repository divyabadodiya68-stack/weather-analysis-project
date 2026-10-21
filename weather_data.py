import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("Weather_Data_Analysis_500_Entries.xlsx",sheet_name="Weather Data")
print(df.head())
# Check rows and columns
print("Dataset Shape:", df.shape)
# Check column names
print("Columns:", df.columns.tolist())
# Check missing values
print(df.isnull().sum())
# Check duplicate rows
print("Duplicate Rows:", df.duplicated().sum())

print("Average Temperature:",
      df["Temperature (°C)"].mean())

print("Maximum Temperature:",
      df["Temperature (°C)"].max())


print("Minimum Temperature:",
      df["Temperature (°C)"].min())

print("Average Humidity:",
      df["Humidity (%)"].mean())

print("Total Rainfall:",
      df["Rainfall (mm)"].sum())
city_temp = df.groupby("City")["Temperature (°C)"].mean()

city_temp.plot(kind="bar", figsize=(10, 5))

plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract month name
df["Month"] = df["Date"].dt.month_name()

# Calculate monthly average temperature
monthly_temp = df.groupby("Month")["Temperature (°C)"].mean()

print("Monthly Average Temperature:")
print(monthly_temp)

plt.figure(figsize=(10, 5))

monthly_temp.plot(kind="line", marker="o")

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# City-wise average temperature
city_temp = df.groupby("City")["Temperature (°C)"].mean()

print("City-wise Average Temperature:")
print(city_temp)

# Create bar chart
plt.figure(figsize=(10, 5))

city_temp.plot(kind="bar", color="skyblue")

plt.title("City-wise Average Temperature")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Calculate total rainfall city-wise
city_rainfall = df.groupby("City")["Rainfall (mm)"].sum()

print("City-wise Total Rainfall:")
print(city_rainfall)

# Find city with maximum rainfall
max_rainfall_city = city_rainfall.idxmax()
max_rainfall = city_rainfall.max()

print("City with Maximum Rainfall:", max_rainfall_city)
print("Maximum Total Rainfall:", max_rainfall, "mm")

# Create bar chart
plt.figure(figsize=(10, 5))

city_rainfall.plot(kind="bar", color="lightgreen")

plt.title("City-wise Total Rainfall")
plt.xlabel("City")
plt.ylabel("Total Rainfall (mm)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Count each weather condition
weather_count = df["Weather Condition"].value_counts()

print("Weather Condition Count:")
print(weather_count)

# Create a bar chart
plt.figure(figsize=(9, 5))

weather_count.plot(kind="bar", color="orange")

plt.title("Weather Condition Analysis")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Occurrences")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Calculate average humidity for each city
city_humidity = df.groupby("City")["Humidity (%)"].mean()

print("City-wise Average Humidity:")
print(city_humidity)

# Find the city with the highest average humidity
highest_city = city_humidity.idxmax()
highest_humidity = city_humidity.max()

print("City with Highest Humidity:", highest_city)
print("Highest Average Humidity:", highest_humidity, "%")

# Create a chart
plt.figure(figsize=(10, 5))

city_humidity.plot(kind="bar", color="mediumpurple")

plt.title("City-wise Average Humidity")
plt.xlabel("City")
plt.ylabel("Average Humidity (%)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Calculate average wind speed city-wise
city_wind = df.groupby("City")["Wind Speed (km/h)"].mean()

print("City-wise Average Wind Speed:")
print(city_wind)

# Create a chart
plt.figure(figsize=(10, 5))

city_wind.plot(kind="bar", color="coral")

plt.title("City-wise Average Wind Speed")
plt.xlabel("City")
plt.ylabel("Average Wind Speed (km/h)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Temperature vs Humidity
plt.figure(figsize=(9, 5))

plt.scatter(
    df["Temperature (°C)"],
    df["Humidity (%)"],
    color="teal",
    alpha=0.7
)

plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))

plt.scatter(
    df["Temperature (°C)"],
    df["Rainfall (mm)"],
    color="darkorange",
    alpha=0.7
)

plt.title("Rainfall vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.tight_layout()
plt.show()


# FINAL WEATHER ANALYSIS REPORT

print("\n===== WEATHER DATA ANALYSIS REPORT =====")

# Overall temperature
print("\nAverage Temperature:",
      round(df["Temperature (°C)"].mean(), 2), "°C")

print("Highest Temperature:",
      df["Temperature (°C)"].max(), "°C")

print("Lowest Temperature:",
      df["Temperature (°C)"].min(), "°C")

# Overall humidity
print("\nAverage Humidity:",
      round(df["Humidity (%)"].mean(), 2), "%")

# Total rainfall
print("\nTotal Rainfall:",
      round(df["Rainfall (mm)"].sum(), 2), "mm")

# City with highest average temperature
city_temp = df.groupby("City")["Temperature (°C)"].mean()

print("\nHottest City:",
      city_temp.idxmax())

# City with highest total rainfall
city_rainfall = df.groupby("City")["Rainfall (mm)"].sum()

print("City with Highest Total Rainfall:",
      city_rainfall.idxmax())

# Most common weather condition
print("Most Common Weather Condition:",
      df["Weather Condition"].mode()[0])

# Data quality checks
print("\nTotal Rows:", len(df))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

print("\n===== REPORT COMPLETED =====")