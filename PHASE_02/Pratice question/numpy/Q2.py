print("===attributes===")
import numpy as np
arr=np.array([[10,20,30],
              [40,50,60]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print("====mathematical operation====")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print("====indexing and slicing====")
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[-1])
print(arr[1:4])
print("====broadcasting====")
a = np.array([10, 20, 30])

print(a + 5)