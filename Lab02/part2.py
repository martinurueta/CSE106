import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])

# Part a A + B
print("Part a")
print(A + B)

# Part b A X B
print("Part b")
print(np.dot(A, B))

# Part c Determinate of A
print("Part c")
print(np.linalg.det(A))

# Part d Inverse of B
print("Part d")
print(np.linalg.inv(B))

# Part e Eigenvalues of A
print("Part e")
print(np.linalg.eigvals(A))

