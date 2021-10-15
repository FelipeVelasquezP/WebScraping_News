import csv
import urllib.request
from io import StringIO
# import datetime

# # current date and time
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days=1)
# yesterdayplus = today - datetime.timedelta(days=2)

# # yesterday = yesterday.strftime("%H:%M:%S")
# print("Hoy:", today)
# print("Ayer:", yesterday)
# print("Antier:", yesterdayplus)

# timestamp1 = yesterday.timestamp()
# timestamp2 = datetime.datetime.timestamp(yesterdayplus)
# print("timestamp de ayer =", timestamp1)
# print("timestamp de antier =", timestamp2)
from datetime import datetime, timedelta

# current date and time
today = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
yesterday = today - timedelta(days=1)
yesterdayplus = today - timedelta(days=2)

print('Hoy = ', today)
print("Ayer:", yesterday)
print("Antier:", yesterdayplus)

timestamp1 = round(datetime.timestamp(yesterdayplus))
timestamp2 = round(datetime.timestamp(yesterday))
print("Antier timestamp =", timestamp1)
print("Ayer timestamp =", timestamp2)

