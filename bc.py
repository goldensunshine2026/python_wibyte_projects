import datetime as dt
import time

print('Welcome to your birthday countdown')

while True:
    try:
        year = int(input('Which year were you born in?\n'))
        month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))
        day = int(input('Which day in that month?\n'))

        current_time = dt.datetime.now()
        current_year = current_time.year

        # Check for a realistic birth year
        if year < current_year - 120:
            print('Please enter a realistic birth year.\n')
            continue

        # Check that the year is not in the future
        if year > current_year:
            print('Birth year must be in the past.\n')
            continue

        # Check that the date is valid
        date_birth = dt.datetime(year, month, day)

        # Check that the birth date is not in the future
        if date_birth > current_time:
            print('Birth date must be in the past.\n')
            continue

        break

    except ValueError:
        print('Invalid date. Please enter a valid date.\n')

weekday_names = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
]

weekday_num = date_birth.weekday()

print('You may have forgotten which day of the week it was ...')
print('But I can tell you ... it was a ...', end=' ')
print(weekday_names[weekday_num])

current_time = dt.datetime.now()
thisyear = current_time.year

# Find next birthday
try:
    thisyear_bday = dt.datetime(thisyear, month, day)
except ValueError:
    # Handles Feb 29 in a non-leap year
    thisyear_bday = dt.datetime(thisyear, 3, 1)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    try:
        next_bday = dt.datetime(thisyear + 1, month, day)
    except ValueError:
        next_bday = dt.datetime(thisyear + 1, 3, 1)

print('Your next birthday will be on ...', end=' ')
print(next_bday)

print()
print('That will be a ...', end=' ')
weekday_num = next_bday.weekday()
print(weekday_names[weekday_num])

print()
print()

while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time

    days_left = dd.days
    total_seconds_left = dd.seconds

    total_mins_left, seconds_left = divmod(total_seconds_left, 60)
    hrs_left, minutes_left = divmod(total_mins_left, 60)

    print(
        'Your next birthday is',
        days_left, 'days',
        hrs_left, 'hrs',
        minutes_left, 'mins',
        seconds_left, 'secs away.',
        end='\r'
    )

    time.sleep(1)

print('\nHappy Birthday!')