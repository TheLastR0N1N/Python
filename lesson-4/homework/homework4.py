# homework

# Write a Python script to sort (ascending and descending) a dictionary by value.

ingredients = {'flour':14,'salt':2,'sugar':4}


ascending_sorted = dict(sorted(ingredients.items(), key=lambda item: item[1]))
descending_sorted = dict(sorted(ingredients.items(), key=lambda item: item[1], reverse = True))




# Write a Python script to add a key to a dictionary.

ingredients['spices'] = 5
ingredients


# Write a Python script to concatenate the following dictionaries to create a new one.


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1 | dic2 | dic3


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input('Enter a number: '))

squared_dict = {x: x * x for x in range(1, n + 1)}
squared_dict


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

dic = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
multiplied_dict = {k: v **2 for k, v in dic.items()}
multiplied_dict

# Write a Python program to create a set.

set = set((1,'a','mjolnir'))
set

# Write a Python program to iterate over sets.

set = {"apple", "banana", "cherry", "date"}

for item in set:
    print(item)


# Write a Python program to add member(s) to a set.

set.add((1,2,3))
set

# Write a Python program to remove item(s) from a given set.

set.discard((1,2,3))
set

# Write a Python program to remove an item from a set if it is present in the set.

set.pop()
