
MAX = 100
def matrixPrint(M, row, col):
   for i in range(row):
      for j in range(col):
         print(M[i][j], end=" ")
      print()

def matrixMultiply(row1, col1, m1, row2, col2, m2):
   res = [[0 for i in range(MAX)] for j in range(MAX)]
   if(row2 != col1):
      print("Matrix multiplication not possible")
      return
   for i in range(row1):
      for j in range(col2):
         res[i][j] = 0
         for k in range(row2):
            res[i][j] += m1[i][k] * m2[k][j]
   print("Result:")
   matrixPrint(res, row1, col2)


if __name__ == "__main__":
   m1 = [[0 for i in range(MAX)] for j in range(MAX)]
   m2 = [[0 for i in range(MAX)] for j in range(MAX)]
   row1 = int(input("Enter the number of rows in matrix 1: "))
   col1 = int(input("Enter the number of columns in matrix 1: "))
   print("Enter the elements of matrix 1:")
   for i in range(row1):
      for j in range(col1):
         m1[i][j] = int(input("m1[" + str(i) + "][" + str(j) + "]: "))

   row2 = int(input("Enter the number of rows in matrix 2: "))
   col2 = int(input("Enter the number of columns in matrix 2: "))

   print("Enter the elements of matrix 2: ")
   for i in range(row2):
      for j in range(col2):
         m2[i][j] = int(input("m2[" + str(i) + "][" + str(j) + "]: "))
   print("Matrix 1: ")
   matrixPrint(m1, row1, col1)
   print("Matrix 2: ")
   matrixPrint(m2, row2, col2)
   matrixMultiply(row1, col1, m1, row2, col2, m2)