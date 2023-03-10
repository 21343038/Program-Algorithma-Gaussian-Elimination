#AbelLevran
#21343038

matrix = [[2, -1, -1],
    [4, 1, -1],
    [1, 1, 1]]

xyzA = [[1],
     [5],
     [0]]
print(matrix[0], xyzA[0])
print(matrix[1], xyzA[1])
print(matrix[2], xyzA[2])
print("\n")
def gaussian_elimination(A, b):
    n = len(A)
    
    # membuat matriks augmented
    aug_matrix = []
    for i in range(n):
        row = A[i] + [b[i]]
        aug_matrix.append(row)
    # mengubah matriks menjadi matriks segitiga atas
    for i in range(n):
        # mencari elemen terbesar pada kolom i
        max_index = i
        for j in range(i+1, n):
            if abs(aug_matrix[j][i]) > abs(aug_matrix[max_index][i]):
                max_index = j

        # menukar baris jika perlu
        aug_matrix[i], aug_matrix[max_index] = aug_matrix[max_index], aug_matrix[i]

        # membuat elemen di bawah pivot menjadi nol
        for j in range(i+1, n):
            factor = aug_matrix[j][i] / aug_matrix[i][i]
            for k in range(i, n+1):
                aug_matrix[j][k] -= factor * aug_matrix[i][k]


    # menghitung solusi menggunakan substitusi mundur
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = aug_matrix[i][n]
        for j in range(i+1, n):
            x[i] -= aug_matrix[i][j] * x[j]
        x[i] /= aug_matrix[i][i]
    return x

#mendeklarasikan matrix 
A = [[2, -1, 1], [4, 1, -1], [1, 1, 1]]
b = [1, 5, 0]
x = gaussian_elimination(A, b)

print("[x,y,z] =",x)
