
import numpy as np

#1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
list = [1,2,3,4,5,6,7,8,9]
arr = np.array(list)

print(arr)

# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

my_list = range(2,11)
matrix = np.array(my_list).reshape(3, 3)

print(matrix)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

a = np.zeros(10)
a[6] = 11
print(a)

# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

range = range(12,39)
arr2 = np.array(range)
print(arr2)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

list2 = [1, 2, 3, 4]
float_array = np.array(list2, dtype=float)
print(float_array) 

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# (0 °C × 9/5) + 32 = 32

temp_c = [0, 12, 45.21, 34, 99.91, 32]
arr_c = np.array(temp_c)
temp_f = (arr_c - 32) * 5/9

rounded_f = np.round(temp_f,2)


print(rounded_f)

# back to celsius

rounded_c = np.round((rounded_f * 9/5) + 32,2)

print(rounded_c)

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.

li = [10, 20, 30]
arr = np.array(li)
li2 = [40,50,60,70,80,90]

arr = np.append(arr, li2)

print(arr)

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

arr = np.array([3,2,7,4,72,5,2,44,53,64])
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print(f'Mean: {mean}\nMedian: {median}\nStandard Deviation: {std}')

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

random = np.random.randint(1, 1000, size=(10, 10))

max = np.max(random)
min = np.min(random)

print(random)
print(f'Max: {max}\nMin: {min}')

# 10
# Create a 3x3x3 array with random values.

random3x = np.random.randint(1,100, size=(3,3,3))

print(random3x)
