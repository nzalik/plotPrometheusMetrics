from datetime import datetime

time_str = "17:42:57.325"

# Assuming today's date for simplicity
date_str = "2024-05-02"

# Combine date and time strings to create a datetime object
datetime_str = date_str + " " + time_str

# Convert the datetime string to a datetime object
dt_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")

# Get the timestamp
timestamp = dt_obj.timestamp()

print("Timestamp:", timestamp)
