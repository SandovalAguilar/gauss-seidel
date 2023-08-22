import gauss_seidel_module as gsm
import numpy as np

raw_matrix = np.random.rand(3,3)
print(raw_matrix.shape[0])
matrix_system = gsm.matrixSystem(raw_matrix, 0.5)

print(raw_matrix)
print(matrix_system.find_diagonal())