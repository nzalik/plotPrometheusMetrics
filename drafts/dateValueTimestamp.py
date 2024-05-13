import datetime

# Convertir le timestamp en une date et heure
#date_time = datetime.datetime.utcfromtimestamp(1714454632.517)
date_time = datetime.datetime.utcfromtimestamp(1714652420)

print("Date et heure correspondant au timestamp 4600 UTC :", date_time)

formatted_time = date_time.strftime("%H:%M:%S")

print("Formatted time (minutes:seconds):", formatted_time)

date_time_local = datetime.datetime.fromtimestamp(1714652420)

print("Date local (UTC):", date_time_local)
