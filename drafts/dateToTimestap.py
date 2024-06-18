from datetime import datetime
#time_str = "12:09:58.023"
time_str = "11:29:14.704"

# Assuming today's date for simplicity
date_str = "2024-06-17"

# Combine date and time strings to create a datetime object
datetime_str = date_str + " " + time_str

# Convert the datetime string to a datetime object
dt_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")

# Get the timestamp
timestamp = dt_obj.timestamp()

print("Timestamp:", timestamp)
