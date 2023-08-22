import numpy as np

class matrixSystem:

    def __init__(self, matrix, tolerance: float):
        self.matrix = matrix
        self.length = self.matrix.shape[0]
        self.tolerance = tolerance
        self.diagonal = self.find_diagonal()
        self.roots_gauss_seidel = self.find_roots_gauss_seidel()
        self.is_dominant = self.verify_diagonal()

    def find_diagonal(self):
        self.diagonal = np.empty((self.length))

        for i in range(self.length):
            self.diagonal[i] = self.matrix[i][i]

        return self.diagonal

    def sum_elements(self):
        sum = 0

        for i in range(self.length):
            sum += self.diagonal[i]

        return sum

    def verify_diagonal(self):
        for i in range(self.length):
            return np.absolute(self.diagonal[i]) > (self.sum_elements() - self.diagonal[i])
                
    def find_roots_gauss_seidel(self):
        from numerical_methods.gauss_seidel_method import gaussSeidel

