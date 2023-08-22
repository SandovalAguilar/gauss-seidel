import numerical_methods as gsm
import numpy as np

raw_matrix = np.random.rand(3,3)
raw_matrix = np.array([[1, 2, 3],
                       [0, 8, 0],
                       [0, 3, 8]])
print(raw_matrix.shape[0])
matrix_system = gsm.matrixSystem(raw_matrix, 0.5)

print(raw_matrix)
print(matrix_system.find_diagonal())
print(matrix_system.sum_elements())
print(matrix_system.verify_diagonal())