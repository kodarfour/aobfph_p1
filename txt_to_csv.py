import json
import csv
import datetime

# Load the JSON file
input_file = "likes.txt"
output_file = "likes.csv"

# Read the JSON data
with open(input_file, "r", encoding="utf-8") as file:
    data = file.read()

# Extract the JSON part from the file (it is wrapped in a JS variable)
json_data = data.split("=", 1)[1].strip()
json_data = json.loads(json_data)

# Function to convert tweetId (Snowflake) to timestamp
def snowflake_to_datetime(snowflake_id):
    timestamp_ms = ((int(snowflake_id) >> 22) + 1288834974657)
    return datetime.datetime.utcfromtimestamp(timestamp_ms / 1000)

# Prepare CSV file
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["tweetId", "timestamp"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    for entry in json_data:
        like = entry.get("like", {})
        tweet_id = like.get("tweetId", "")
        timestamp = snowflake_to_datetime(tweet_id) if tweet_id else ""

        writer.writerow({
            "tweetId": tweet_id,
            "timestamp": timestamp
        })

print(f"CSV file created: {output_file}")
