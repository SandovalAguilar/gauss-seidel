import numpy as np

class matrixSystem:

    def __init__(self, matrix, tolerance: float):
        self.matrix = matrix
        self.length = self.matrix.shape[0]
        self.tolerance = tolerance
        self.diagonal = self.find_diagonal()
        # This is the actual function that applies the Gauss-Seidel method 
        self.roots = self.find_roots()
        self.is_dominant = self.verify_diagonal()

    def find_diagonal(self):
        self.diagonal = np.empty((self.length))

        for i in range(self.length):
            self.diagonal[i] = self.matrix[i][i]

        return self.diagonal

    def verify_diagonal():
        pass

    def find_roots(self):
        pass

