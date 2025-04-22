import datetime
from datetime import date,time,datetime,timezone,timedelta

# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

# user_birth_date = input('Enter your birth date in the following format: dd/mm/yyyy')
# birth_date = datetime.strptime(user_birth_date,'%d/%m/%Y')

# today = date.today()
# age = today.year - birth_date.year


# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     age -= 1
# print(age)

# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

# user_birth_date = input('Enter your birth date in the following format: dd/mm/yyyy')
# birth_date = datetime.strptime(user_birth_date,'%d/%m/%Y')

# today = date.today()
# age = today.year - birth_date.year


# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     age -= 1

# if age == today.year - birth_date.year:
#     if (birth_date.month, birth_date.day) != (2,29):
#         print(date(birth_date.year + age + 1, birth_date.month, birth_date.day))
#     if (birth_date.month, birth_date.day) == (2,29):
#         print(date(birth_date.year + age + 1, birth_date.month, birth_date.day - 1))

# if age < today.year - birth_date.year:
#         if (birth_date.month, birth_date.day) != (2,29):
#             print(date(birth_date.year + age + 1, birth_date.month, birth_date.day))
#         if (birth_date.month, birth_date.day) == (2,29): 
#             print(date(birth_date.year + age + 1, birth_date.month, birth_date.day - 1))   

# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

# 
# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
# Without considering next day, next month, next year or leap years

# current_date = input('Enter the date in the following way: dd/mm/yyyy')
# current_time = input('Enter the time in the following way: hh:mm')
# timespan = int(input('How long do you want the meeting to last? (hours)'))

# current_date = datetime.strptime(current_date, '%d/%m/%Y').date()
# current_time = datetime.strptime(current_time, '%H:%M').time()
# timespan_hour = time(timespan,00)

# print(current_date, time(timespan_hour.hour + current_time.hour,current_time.minute))

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

# import pytz
# region_tz = input('Enter the region TimeZone: ')
# city_tz = input('Enter the city TimeZone: ')

# corrected_city = city_tz.replace('_',' ')

# local = print('Tashkent:',datetime.now().strftime('%d-%B/%Y %H:%M:%S'))

# input_tz = pytz.timezone(f'{region_tz}/{city_tz}')
# tz_output = print(f'{corrected_city}:',datetime.now(input_tz).strftime('%d-%B/%Y %H:%M:%S'))

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

# future_datetime1 = input('Enter the date: dd/mm/yyyy HH:MM:SS')

# future_datetime = datetime.strptime(future_datetime1,'%d/%m/%Y %H:%M:%S')

# while True:
#     now = datetime.now()

#     if future_datetime <= now:
#         print('Time\'s up')
#         break

#     years = future_datetime.year - now.year
#     months = future_datetime.month - now.month
#     days = future_datetime.day - now.day
#     hours = future_datetime.hour - now.hour
#     minutes = future_datetime.minute - now.minute
#     seconds = future_datetime.second - now.second

#     if seconds < 0:
#         seconds += 60
#         minutes -= 1
#     if minutes < 0:
#         minutes += 60
#         hours -= 1
#     if hours < 0:
#         hours += 24
#         days -= 1
#     if days < 0:
#         days += 30
#         months -= 1
#     if months < 0:
#         months += 12
#         years -= 1

#     print(f"Time remaining: {years}y {months}m {days}d {hours}h {minutes}m {seconds}s", end='\r')
#     time.sleep(1)

# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

# import re

# email = input('Enter the email: ')

# pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

# if re.fullmatch(pattern, email):
#     print("Valid email!")
# else:
#     print("Invalid email.")

# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

import re


# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

# import re

# password = input('Input the password')

# pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{10,}$'

# if re.fullmatch(pattern, password):
#     print('The password is valid')
# else:
#     print('Invalid')

# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

# word = input('Enter the word: ')

# sample = 'Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals'

# matches = re.findall(r'\b' + re.escape(word) + r'\b', sample)

# print(f"Occurrences of '{word}': {matches}")

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.



sample = 'Countdown Timer: Implement a countdown timer. 27/03/2025 Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals'


date_pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})\b'

dates = re.findall(date_pattern, sample)

if dates:
    print('Extracted dates:', dates)
else:
    print('No dates found in the text.')
