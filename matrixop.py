# Addition of two matrices
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

# Initialize matrices
matrixa = []
matrixb = []
resultmatrix = []

print("Enter the entries row wise:")
# For user input
print("Enter the entries for matrix A:")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrixa.append(a)

# For printing first matrix
print("First matrix:")
for i in range(row):
    for j in range(col):
        print(format(matrixa[i][j], "<3"), end=" ")
    print()

print("Enter entries for matrix B:")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrixb.append(a)

# For printing second matrix
print("Second matrix:")
for i in range(row):
    for j in range(col):
        print(format(matrixb[i][j], "<3"), end=" ")
    print()

# For matrix addition
for i in range(row):
    a = []
    for j in range(col):
        a.append(matrixa[i][j] + matrixb[i][j])
    resultmatrix.append(a)

print("Addition of both matrices:")
# For printing the result matrix
for i in range(row):
    for j in range(col):
        print(format(resultmatrix[i][j], "<3"), end=" ")
    print()

# Multiplication of two matrices
row1 = int(input("Enter the number of rows:"))
col1 = int(input("Enter the number of columns:"))
c = 0

# Initialize matrices
matrixa = []
matrixb = []
resultmatrix = []

print("Enter the entries rowwise:")
# For user input
print("Enter the entries for matrix A:")
for i in range(row1):
    a = []
    for j in range(col1):
        a.append(int(input()))
    matrixa.append(a)

# For printing first matrix
print("Matrix A:")
for i in range(row1):
    for j in range(col1):
        print(format(matrixa[i][j], "<3"), end=" ")
    print()

print("Enter entries for matrix B:")
row2 = int(input("Enter the number of rows:"))
col2 = int(input("Enter the number of columns:"))

for i in range(row2):
    a = []
    for j in range(col2):
        a.append(int(input()))
    matrixb.append(a)

# For printing second matrix
print("Matrix B:")
for i in range(row2):
    for j in range(col2):
        print(format(matrixb[i][j], "<3"), end=" ")
    print()

# For matrix multiplication
for i in range(row1):
    a = []
    for j in range(col2):
        for k in range(row2):
            c = c + matrixa[i][k] * matrixb[k][j]
        a.append(c)
        c = 0
    resultmatrix.append(a)

print("Result matrix for multiplication:")
# For printing the result matrix
for i in range(row1):
    for j in range(col2):
        print(format(resultmatrix[i][j], "<3"), end=" ")
    print()

# Subtraction of two matrices
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

# Initialize matrices
matrixa = []
matrixb = []
resultmatrix = []

print("Enter the entries row wise:")
# For user input
print("Enter the entries for matrix A:")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrixa.append(a)

# For printing first matrix
print("First matrix:")
for i in range(row):
    for j in range(col):
        print(format(matrixa[i][j], "<3"), end=" ")
    print()

print("Enter entries for matrix B:")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrixb.append(a)

# For printing second matrix
print("Second matrix:")
for i in range(row):
    for j in range(col):
        print(format(matrixb[i][j], "<3"), end=" ")
    print()

# For matrix subtraction
for i in range(row):
    a = []
    for j in range(col):
        a.append(matrixa[i][j] - matrixb[i][j])
    resultmatrix.append(a)

print("Subtraction of both matrices:")
# For printing the result matrix
for i in range(row):
    for j in range(col):
        print(format(resultmatrix[i][j], "<3"), end=" ")
    print()

# Transpose of a matrix
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

# Initialize matrices
matrixa = []
result = []

print("Enter the entries rowwise:")
# For user input
print("Enter the entries for matrix A:")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrixa.append(a)

# For printing matrix
print("Matrix A:")
for i in range(row):
    for j in range(col):
        print(matrixa[i][j], end=" ")
    print()

# result matrix
for i in range(col):
    a = []
    for j in range(row):
        a.append(0)
    result.append(a)

# Transpose of matrix
for i in range(row):
    for j in range(col):
        result[j][i] = matrixa[i][j]

# print result
print("Result matrix for transpose of matrix:")
for i in range(col):
    for j in range(row):
        print(result[i][j], end=" ")
    print()
