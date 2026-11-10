import numpy as np
arr=np.array([1,2,3,4,5])
print("Array: ",arr)
print(arr[0])
print(arr[4])
print(arr[2])
print(arr[-1])
# Slicing
print(arr[1:4])
print(arr[:3])
print(arr[2:])


'''
Using this array:
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])



Find the output using indexing and slicing:
1. arr[0]
2. arr[3]
3. arr[-1]
4. arr[1:5]
5. arr[:4]
6. arr[3:]
'''

arr=np.array([5, 10, 15, 20, 25, 30, 35, 40])
print("Array is: ",arr)
print(arr[0])
print(arr[3])
print(arr[-1])
print(arr[1:5])
print(arr[:4])
print(arr[3:])

# 2D NumPy indexing
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("2D Array is: ",arr)
print(arr[0, 1])
print(arr[1, 0])
print(arr[2, 2])
print(arr[0, :])
print(arr[:, 1])
print(arr[:, 2])