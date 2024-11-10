matrix = [
    [31, 65, -83, -2, -85],
    [9, -2, 11, -4, 70],
    [52, 73, -8, -1, 60],
    [57, 83, -1, 82, 50],
    [1, -3, -2, 78, -9]
]

def sort(func):
    def sort_matrix(matrix):
        func(matrix)
        return matrix
    return sort_matrix

@sort
def sort_by_insertion(matrix):
    for column in range(len(matrix[0])): 
        for i in range(1, len(matrix)):
            x = matrix[i][column]  
            j = i - 1
            while j >= 0 and matrix[j][column] > x:
                matrix[j + 1][column] = matrix[j][column]
                j -= 1
            matrix[j + 1][column] = x

sorted_matrix = sort_by_insertion(matrix)
print("Sorted matrix by columns:")
for row in sorted_matrix:
    print(row)
    
def calculate_fi(matrix):
    fi= []
    for i in range(len(sorted_matrix)):
        row_sum = sum(sorted_matrix[i][j] for j in range(i + 1, len(sorted_matrix[i])))
        fi.append(row_sum)
    return fi
fi = calculate_fi(matrix)
def calculate_F(fi):
    product = 1
    count = len(fi)
    for value in fi:
        product *= abs(value) if value != 0 else 1 
    return product ** (1 / count) if count > 0 else 0
F_value = calculate_F(fi)
print(f"Sums of elements above the main diagonal for each row:", fi)
print("Geometric sum of sums of elements above the main diagonal for each row", round( F_value, 3))
