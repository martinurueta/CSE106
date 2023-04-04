import numpy as np
# Part a
print("Part a")
mat = np.arange(2,10).reshape(4,2)
print(mat)

# Part b
print("Part b")
mat = np.zeros((8,8), dtype=int)
mat[::2, ::2] = 1
mat[1::2, 1::2] = 1
print(mat)

# Part c
print("Part c")
arr = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
print(np.unique(arr))

# Part d
print("Part d")
arr = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
result = arr[arr > 37]
print(result)

# Part e
print("Part e")
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

arr = [0, 12, 45.21, 34, 99.91]
arr = np.array(arr)
print(celsius_to_fahrenheit(arr))