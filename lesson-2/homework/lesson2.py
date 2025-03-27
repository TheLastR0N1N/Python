# homework
# 

# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("What is your name? ")
year_of_birth = int(input("What year were you born? "))
current_year = 2025
age = current_year - year_of_birth
print(f'Hello, I am {name}, i am {age} years old.')


# Extract car names from the following text:

txt = 'LMaasleitbtui'
print(txt[::2], txt[1::2])


# Extract car names from the following text:

txt = 'MsaatmiazD'
txt1 = txt[1:]
car_name1 = txt[::2]
car_name2 = txt1[::-2]
print(car_name1,car_name2)

# Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt1 = txt[-6:]
txt1

# Write a Python program that takes a user input string and prints it in reverse order.

msg = input('Enter your message.')
rev_msg = msg[::-1]
print(f'Here\'s the message: {msg}. Here\'s the reversed message: {rev_msg}')

# Write a Python program that counts the number of vowels in a given string.

str = input('Insert your message')
count_a = str.count('a')
count_e = str.count('e')
count_i = str.count('i')
count_o = str.count('o')
count_u = str.count('u')
count_y = str.count('y')
sum = count_a + count_e + count_i + count_o + count_u + count_y 

print(f'Number of vowels = {sum}')

# Write a Python program that takes a list of numbers as input and prints the maximum value.

No1 = int(input('Enter the number'))
No2 = int(input('Enter the number'))
No3 = int(input('Enter the number'))
No4 = int(input('Enter the number'))
No5 = int(input('Enter the number'))
numbers = [No1, No2, No3, No4, No5]
max_numbers = max(numbers)

print(f'Max number is {max_numbers}')

# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input('Enter the word: ')
lowered_word = word.lower()
if lowered_word == lowered_word[::-1]:
    print(f'The word {word} is a palindrome')
else:
    print(f'The word {word} is not a palindrome')



# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input('Enter your email: ')
sym_loc = email.find('@')
domain = email[sym_loc+1:]
print(f'Your domain is {domain}')

# Write a Python program to generate a random password containing letters, digits, and special characters.
 
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()1234567890"
password = ""

for i in range(12):
        password += random.choice(characters)

print(password)        

