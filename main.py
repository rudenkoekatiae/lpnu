from enum import Enum

class ComparisonMethod(Enum):
    ELEMENTWISE = 1
    SIZE = 2
    SUM = 3
    MAX = 4

class Matrix:
    def __init__(self):
        self.matrix1 = [
            [31, 65, -83, -2, -85],
            [9, -2, 11, -4, 70],
            [52, 73, -8, -1, 60],
            [57, 83, -1, 82, 50],
            [1, -3, -2, 78, -9]
        ]
        
        self.matrix2 = [
            [25, 12, -6, 63, 2],
            [32, -85, -7, -6, 99],
            [1, 73, 52, -12, -3],
            [2, 3, 5, 81, -6],
            [-1, -2, -3, -6, 15]
        ]

    def sort(func):
        def sort_matrix(self, matrix):  
            sorted_matrix = func(self, matrix)
            return sorted_matrix
        return sort_matrix

    @sort
    def sort_by_insertion(self, matrix):
        for column in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                x = matrix[i][column]
                j = i - 1
                while j >= 0 and matrix[j][column] > x:
                    matrix[j + 1][column] = matrix[j][column]
                    j -= 1
                matrix[j + 1][column] = x
        return matrix

    def calculate_fi(self, matrix):
        fi = []
        for i in range(len(matrix)):
            row_sum = sum(matrix[i][j] for j in range(i + 1, len(matrix[i])))
            fi.append(row_sum)
        return fi

    def calculate_F(self, fi):
        product = 1
        for value in fi:
            product *= abs(value) if value != 0 else 1
        return product ** (1 / len(fi)) if fi else 0

    def sum_of_matrices(self):
        if len(self.matrix1) != len(self.matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(self.matrix1, self.matrix2)):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return [[self.matrix1[i][j] + self.matrix2[i][j] for j in range(len(self.matrix1[0]))] for i in range(len(self.matrix1))]
    
    def subtract_matrices(self):
        if len(self.matrix1) != len(self.matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(self.matrix1, self.matrix2)):
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        return [[self.matrix1[i][j] - self.matrix2[i][j] for j in range(len(self.matrix1[0]))] for i in range(len(self.matrix1))]


class MatrixComparer:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def compare_matrices(self, method):

        if method == ComparisonMethod.ELEMENTWISE:
            return "Matrices are identical" if self.matrix1 == self.matrix2 else "Matrices are different"
        
        elif method == ComparisonMethod.SIZE:
            return "Matrices have the same size" if len(self.matrix1) == len(self.matrix2) and \
                   all(len(row1) == len(row2) for row1, row2 in zip(self.matrix1, self.matrix2)) else "Matrices have different sizes"

        elif method == ComparisonMethod.SUM:
            sum_matrix1 = sum(sum(row) for row in self.matrix1)
            sum_matrix2 = sum(sum(row) for row in self.matrix2)
            return ("matrix1 is greater by sum" if sum_matrix1 > sum_matrix2 else
                    "matrix2 is greater by sum" if sum_matrix2 > sum_matrix1 else "Both matrices are equal by sum")

        elif method == ComparisonMethod.MAX:
            max_matrix1 = max(max(row) for row in self.matrix1)
            max_matrix2 = max(max(row) for row in self.matrix2)
            return ("matrix1 is greater by max element" if max_matrix1 > max_matrix2 else
                    "matrix2 is greater by max element" if max_matrix2 > max_matrix1 else "Both matrices are equal by max element")


matrix_instance = Matrix()

sorted_matrix1 = matrix_instance.sort_by_insertion(matrix_instance.matrix1)
fi_1 = matrix_instance.calculate_fi(sorted_matrix1)
F_value1 = matrix_instance.calculate_F(fi_1)

sorted_matrix2 = matrix_instance.sort_by_insertion(matrix_instance.matrix2)
fi_2 = matrix_instance.calculate_fi(sorted_matrix2)
F_value2 = matrix_instance.calculate_F(fi_2)

print("Sorted columns of matrix1:")
for row in sorted_matrix1:
    print(row)
print("Sum of elements above the main diagonal for each row for matrix1:", fi_1)
print("Geometric sum of sums of elements above the main diagonal for each row for matrix1:", round(F_value1, 3))

print("\nSorted columns of matrix2:")
for row in sorted_matrix2:
    print(row)
print("Sum of elements above the main diagonal for each row for matrix2:", fi_2)
print("Geometric sum of sums of elements above the main diagonal for each row for matrix2:", round(F_value2, 3))

try:
    suma = matrix_instance.sum_of_matrices()
    print("\nSum of matrices:")
    for row in suma:
        print(row)
except ValueError:
    print("Matrices cannot be added due to size mismatch.")

try:
    subs = matrix_instance.subtract_matrices()
    print("\nDifference of matrices:")
    for row in subs:
        print(row)
except ValueError:
    print("Matrices cannot be subtracted due to size mismatch.")

matrix_comparer = MatrixComparer(matrix_instance.matrix1, matrix_instance.matrix2)
print("\nMatrix comparisons:")
print("Elementwise:", matrix_comparer.compare_matrices(method=ComparisonMethod.ELEMENTWISE))
print("Same size:", matrix_comparer.compare_matrices(method=ComparisonMethod.SIZE))
print("Comparison by sum:", matrix_comparer.compare_matrices(method=ComparisonMethod.SUM))
print("Comparison by max element:", matrix_comparer.compare_matrices(method=ComparisonMethod.MAX))