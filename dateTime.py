import datetime
import pytz

today = datetime.date.today()

days_since_birth = datetime.date(1999, 2, 6)

# Total days that u lived
print((today - days_since_birth).days)

# adding 10 days in current date
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

# print(today.day)

# monday = 0, sunday = 7
print(today.weekday())

print(datetime.time(7, 6, 7, 8))

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_india = datetime_today.astimezone(pytz.timezone('Indian/Maldives'))
print(datetime_india)

# for tz in pytz.all_timezones:
#     print(tz)


# formatting datetime object into string
# strftime() where f stands for formatting

print(datetime_india.strftime('%B %d, %Y'))

# now converting string date into object
# strptime() where p stands for parsing

datetime_thing = datetime.datetime.strptime('April 21, 2021', '%B %d, %Y')
print(datetime_thing)