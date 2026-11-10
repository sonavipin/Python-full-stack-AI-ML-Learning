import numpy as np
numbers=np.array([1,2,3,4,5])
print(numbers)
print(type(numbers))

arr_1d=np.array([10,20,30,40,50])
print("1D array: ",arr_1d)

arr_2d=np.array([[1,2,3],[4,5,6]])
print("2D array: ",arr_2d)
print(arr_2d.ndim)
print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.dtype)

'''
Create a two-dimensional NumPy array containing these values:
10 20 30
40 50 60
70 80 90

Then print:
1. The array
2. Number of dimensions
3. Shape
4. Total number of elements
5. Data type
'''
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Array is: ",arr)
print("Number diamension: ",arr.ndim)
print("Shape: ",arr.shape)
print("Total number of elements: ",arr.size)
print("Data type: ",arr.dtype)