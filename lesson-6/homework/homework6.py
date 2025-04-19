# 1. Modify String with Underscores
def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0
    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            if txt[i] not in vowels and (i + 1 >= len(txt) or txt[i + 1] != '_'):
                result.append('_')
                count = 0
            else:
                count = 2
        i += 1
    # Remove trailing underscore if exists
    if result and result[-1] == '_':
        result.pop()
    return ''.join(result)

print(insert_underscores("hello"))         # hel_lo
print(insert_underscores("assalom"))       # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef


# 2. Integer Squares Exercise
n = 5
for i in range(n):
    print(i**2)


# 3. Loop-Based Exercises

# Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3
num = 10
total = sum(range(1, num + 1))
print("Sum is:", total)

# Exercise 4
num = 2
for i in range(1, 11):
    print(num * i)

# Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        continue
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

# Exercise 6
number = 75869
print("Output:", len(str(number)))

# Exercise 7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9
for i in range(-10, 0):
    print(i)

# Exercise 10
for i in range(5):
    print(i)
print("Done!")

# Exercise 11
start, end = 25, 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12
n_terms = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end="  ")
    a, b = b, a + b
print()

# Exercise 13
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

num = 5
print(f"{num}! = {factorial(num)}")


# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for key in c1:
        if key not in c2:
            result.extend([key] * c1[key])
    for key in c2:
        if key not in c1:
            result.extend([key] * c2[key])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))           # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))           # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]
