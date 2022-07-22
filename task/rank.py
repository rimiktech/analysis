#-Write a program to import the numpy and find 
#1-Rank of a matrix 
#2-Trace of matrix A
#3-Determinant of a matrix  
#4-Inverse of matrix A
#using this function "numpy.linalg.eig(a) "
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 

print("Rank of A:", np.linalg.matrix_rank(A))
 

print("\nTrace of A:", np.trace(A))
 

print("\nDeterminant of A:", np.linalg.det(A))
 

print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))