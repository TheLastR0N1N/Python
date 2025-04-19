import os

# === Exception Handling Exercises ===

# 1. Handle ZeroDivisionError
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide_numbers(5, 0)

# 2. Raise ValueError for invalid integer input
def get_integer():
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
    except ValueError:
        print("Error: Invalid integer.")

# get_integer()

# 3. Handle FileNotFoundError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")

read_file("non_existing_file.txt")

# 4. Raise TypeError if inputs aren't numbers
def input_two_numbers():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
            raise TypeError("Inputs must be numbers.")
        print("Sum is:", float(a) + float(b))
    except TypeError as e:
        print("Error:", e)

# input_two_numbers()

# 5. Handle PermissionError
def open_file_permission_test(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Testing permissions.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")

open_file_permission_test("/root/test.txt")  # Adjust path on Windows/Linux


# === File Input/Output Exercises ===

sample_file = "sample.txt"
with open(sample_file, "w") as f:
    f.write("This is a sample file.\nWith multiple lines.\nSome more text here.\nAnd some more.")

# 1. Read entire text file
def read_entire_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

read_entire_file(sample_file)

# 2. Read first n lines
def read_first_n_lines(filename, n):
    with open(filename, 'r') as f:
        for _ in range(n):
            print(f.readline(), end='')

read_first_n_lines(sample_file, 2)

# 3. Append text to a file and display
def append_and_display(filename, text):
    with open(filename, 'a') as f:
        f.write("\n" + text)
    with open(filename, 'r') as f:
        print(f.read())

append_and_display(sample_file, "Appended line.")

# 4. Read last n lines of a file
def read_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line, end='')

read_last_n_lines(sample_file, 2)

# 5. Read line by line into list
def file_to_list(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    print(lines)

file_to_list(sample_file)

# 6. Read file into a variable
def file_to_variable(filename):
    with open(filename, 'r') as f:
        content = f.read()
    print(content)

file_to_variable(sample_file)

# 7. Read line by line into array
def file_to_array(filename):
    arr = []
    with open(filename, 'r') as f:
        for line in f:
            arr.append(line.strip())
    print(arr)

file_to_array(sample_file)

# 8. Find longest word(s)
def longest_words(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
        max_len = max(len(word) for word in words)
        print([word for word in words if len(word) == max_len])

longest_words(sample_file)

# 9. Count number of lines
def count_lines(filename):
    with open(filename, 'r') as f:
        print("Number of lines:", len(f.readlines()))

count_lines(sample_file)

# 10. Count word frequency
def word_frequency(filename):
    from collections import Counter
    with open(filename, 'r') as f:
        words = f.read().split()
        freq = Counter(words)
    print(freq)

word_frequency(sample_file)

# 11. Get file size
def file_size(filename):
    size = os.path.getsize(filename)
    print("File size in bytes:", size)

file_size(sample_file)
