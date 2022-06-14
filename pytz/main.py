import datetime
import pytz

eastern = pytz.timezone("US/Eastern")
amsterdam = pytz.timezone("Europe/Amsterdam")

local_time = datetime.datetime.now()
print(local_time)
eastern_time = eastern.localize(local_time)
print(eastern_time)

amsterdam_time = eastern_time.astimezone(amsterdam)
print(amsterdam_time)

utc_local_time = datetime.datetime.now(tz=pytz.utc)
print(utc_local_time)