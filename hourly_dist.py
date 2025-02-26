import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("likes.csv", parse_dates=["timestamp"])

# Extract hour from timestamps
df["hour"] = df["timestamp"].dt.hour

# Group by hour to count likes
hourly_distribution = df.groupby("hour").size()

# Plot the hourly distribution
plt.figure(figsize=(10, 5))
plt.bar(hourly_distribution.index, hourly_distribution.values, width=0.8, edgecolor="black")
plt.xlabel("Hour of the Day (UTC)")
plt.ylabel("Number of Likes")
plt.title("Distribution of Twitter Likes by Hour")
plt.xticks(range(0, 24))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
