import numpy as np
np.set_printoptions(precision=4, suppress=True)  # set parameters of printing i numpy library

############## NORM OF VECTOR / LENGTH OF VECTOR #############
"""
v1 = np.array([-1, 4])
print(v1)

norm_of_vector = np.linalg.norm(v1)  # "linalg" module from NumPy library -- "norm" functions is usued to calculate....
# ... norm of vector// calculating of v1 vector length
print(norm_of_vector)

v2 = np.array([-10, 10, 13])  # vector in "v2" three-dimensional space
norm_of_vector2 = np.linalg.norm(v2)
print(norm_of_vector2)


#################### DISTANCE BETWEEN POINTS ON SPACE ########################

p = np.array([0, 3])
q = np.array([4, 0])

distance_p_q = np.linalg.norm(p-q)  # distance between dwo points on R2 space
print(distance_p_q, "\n")

p = np.array([0, 3, 2])
q = np.array([4, 0, 1])

distance_p_q = np.linalg.norm(p-q)  # distance between dwo points on R3 space
print(distance_p_q, "\n")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

A = np.array(
    [[5, 3],
     [3, 9]])

B = np.array(
    [[1],
     [-1]])
print(A, "\n\n", B, "\n")

AB = np.dot(A, B)  # "dot" function is uses to multiply matrixs/arrays
print(AB, "\n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

Q = np.array(
    [[2, -1, 3],
     [3, 1, 0]])
W = np.array(
    [[2, 1, -1],
     [0, -1, 2],
     [3, 2, 0]])
print(Q, "\n\n", W, "\n")

QW = np.dot(Q, W)
print("QW =\n", QW)


################ DETERMINANT(wyznacznik) OF MATRIX, IDENTITY(jednostkowa), INVERSE, TRANSPOSE MATRIX ##########

W = np.array(
    [[2, 1, -1],
     [0, -1, 2],
     [3, 2, 0]])
print(np.linalg.det(W))  # "det" function is uses tp calculate a determinant of matrix -D
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

print(np.eye(5, dtype="int"))  # "eye" function is uses to creating IDENTITY(jednostkowa) MATRIX

print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

A = np.array(
    [[5, 3],
     [3, 9]])

B = np.linalg.inv(A,)  # "inv" function creates INVERSE MATRIX to matrix A - INVERSE MATRIX CAN'T BE CALCULATE FOR...
# ..SINGULAR MATRIX (MACIERZ OSOBLIWA) - this is matrix which has determinant equal 0 det(A) = 0
print(B, "\n")
# moreover, exists relaton between matrix A, inverse matrix to them B and identity matrix I: AB=BA=I :
np.set_printoptions(precision=4, suppress=True)  # set parameters of printing i numpy library
print(np.dot(A, B))  # results of multiply matrix A and inverse matrix B is IDENTITY matrix

print("^^^^^^^^^^^^^^^^^^^^^^")

Q = np.array(
    [[2, -1, 3],
     [3, 1, 0]])

print(Q.T)  # "T" function is uses to TRANSPOSing matrix


############### SOLVING SYSTEMS OF EQUATIONS ############################

##### x + y = 6
##### -3x +y = 2

## To solve systmes od equations by matrix should use this relation:
#                           A * X = B
#                           X = A_inverse * B
#                           below is used this relation to solve above equation:

A = np.array([[1, 1],
              [-3, 1]])
print(A, "\n")
B = np.array([[6], [2]])
print(B, "\n")

A_inv = np.linalg.inv(A)
print(A_inv, "\n")

X = np.dot(A_inv, B)
print(X)
"""
######## STATISTIC FUNCTIONS ############################

price = np.array([[12.40, 12.80, 11.90, 12.60, 1000],
                  [12.50, 13.00, 11.70, 12.20, 2000],
                  [12.20, 13.40, 12.20, 13.20, 1500]])
print(price, "\n")

print(price.sum(axis=0), "\n")  # "sum" function is used to calculate sum of elements chose by "axis" parameter - if "axis" ..
# = 0, we get sum of each columns in array "price", if axis = 1, we get sum of each rows

print(price.sum(axis=1), "\n")

print(np.sum(price), "\n")

print(np.min(price), "\n")

print(np.max(price, axis=1), "\n")

print(np.median(price, axis=0), "\n")

print(np.mean(price, axis=0), "\n")

print(np.std(price, axis=0), "\n")  # STANDARD DEVIATION (ODCHYLENIE STANDARDOWE)

print(np.var(price, axis=1), "\n")  # VARIANCE - Wariancja liczb x1,x2,...,xn to średnia arytmetyczna kwadratów...
#  odchyleń od ich średniej arytmetycznej:
#                    σ2=((x1−X¯)^2+(x2−X¯)^2+...+(xn−X¯)^2)


