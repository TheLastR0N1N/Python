
# Create a list containing five different fruits and print the third fruit.
fruits = ['Apple', 'Pineapple', 'Strawberry', 'Pear', 'Grapes']
print(fruits[2])


# Create two lists of numbers and concatenate them into a single list.
n1 = [1, 2, 3, 4, 5, 6]
n2 = [7, 8, 9]
n = n1 + n2
print(n)

# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

n1 = [1, 2, 3, 4, 5, 6, 7, 8]
first = n1[0]
middle = int(len(n1) / 2) + 1
last = n1[-1]
n = [first, middle, last]
print(n)

# Create a list of your five favorite movies and convert it into a tuple.

movies = ['Kingsman', 'Invincible', 'The Boys', 'Stranger Things', 'Breaking Bad']
movies_tuple = tuple(movies)
print(movies_tuple)

# Given a list of cities, check if "Paris" is in the list and print the result.

cities = ['Paris', 'London', 'New York', 'Berlin', 'Rome']
'Paris' in cities

# Create a list of numbers and duplicate it without using loops.

n1 = [1, 2, 3, 4, 5, 6, 7, 8]
nc = n1.copy()

# Given a list of numbers, swap the first and last elements.

numbers = [10, 20, 30, 40, 50]

# Swapping first and last element
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)


# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

no = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced = no[2:7]
sliced


# Create a list of colors and count how many times "blue" appears in the list.

colors = ['Blue', 'Green', 'Yellow', 'Blue', 'Blue', 'Black', 'White']
colors.count('Blue')


# Given a tuple of animals, find the index of "lion".

animals = ("tiger", "elephant", "lion", "zebra", "giraffe")
animals.index("lion")



# Create two tuples of numbers and merge them into a single tuple.

numbers1 = (1,2,3,4,5,6,7,8,9,0)
numbers2 = (1,2,3,4,5,6,7,8,9,0)
num = numbers1 + numbers2
print(num) 

# Given a list and a tuple, find and print their lengths.

numbers1 = (1,2,3,4,5,6,7,8,9,10)
numbers3 = [1,2,3,4,5,6,7,8,9,0]
len(numbers1), len(numbers3)


# Create a tuple of five numbers and convert it into a list.

numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)

print(numbers_list)


# Given a tuple of numbers, find and print the maximum and minimum values.

numbers1 = (1,2,3,4,5,6,7,8,9,10)
max(numbers1), min(numbers1)

# Create a tuple of words and print it in reverse order.

animals = ("tiger", "elephant", "lion", "zebra", "giraffe")
reversed = animals[::-1]
reversed


