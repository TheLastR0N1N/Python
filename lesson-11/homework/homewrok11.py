import math

# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

import math


# Circle Area Formula: A = π*r^2

def area(r):
    return math.pi * (r ** 2)

# Circle Length Formula: C=2πr

def length(r):
    return math.pi * 2 * r

# circle.py

# file_reader.py
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


from math_operations import add, subtract,power
from string_utils import reverse_string, count_vowels
from geometry.circle import area, length
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file


print(add(5, 3))  
print(subtract(5, 3))  
print(power(5, 3)) 

print(reverse_string("hello"))  
print(count_vowels("hello"))  

r = 5
print(area(r))  
print(length(r)) 

write_file("example.txt", "Hello, this is a test.")
content = read_file("example.txt")
print(content)  
