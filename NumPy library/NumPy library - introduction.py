import numpy as np

################ NumPy - ARRAYS #####################################
"""
print(dir(np))
print(np.__version__)

x = np.array([1, 2])
print(type(x), "\n", x, "\n")

x = np.array([[2, -4], [3, 4]])

print(x)

print(x.ndim)
print(x.shape)
print(x.dtype)

print("\n")

x = np.array(
    [[[3, 2, 4],
      [3, 4, 5]],

      [[-1, 5, 3],
     [6, 4, 2]],

    [[3, 5, 6],
    [3, 5, 2]]]
)

print(x)
print("\n")

print(x.ndim)
print(x.shape)
print(x.dtype)

################ Basic data types in NumPy #####################################

A = np.array([2, 5, 8])
print(A.dtype)
print(A, "\n")

A = np.array([2, 5, 8], dtype='complex')
print(A.dtype)
print(A, "\n")

B = np.array([True, False])
print(B)
print(B.ndim)
print(B.shape)
print(B.dtype)

#################### NumPy - arrays CREATING ######################

A = np.zeros(shape=(5, 4))

print(A)
print(A.dtype)

A = np.zeros(shape=(5, 4))

A = np.zeros(shape=(5, 4), dtype='int')
print(A)
print(A.dtype)

B = np.ones(shape=(5, 5), dtype='int')
print(B)
print(B.dtype)

C = np.full(shape=(3, 3), fill_value=4, dtype='float')
print(C)
print(C.dtype)

D = np.arange(10)
print(D)

print(np.arange(start=4, stop=9))

print(np.arange(start=10, stop=100, step=10))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
X = np.arange(15)
print(X)
Q = X.reshape(5, 3)  # change a list to array/matrix which have 5 rows and 3 columns
print(Q)
print("^^^^^^^^^^^^^^^^^^^^")
print(X.reshape(3, -1))

print("^^^^^^^^^^^^^^^^^^^^")
print(X.reshape(-1, 3))


###################### Basic operations on ARRAYS ##################3

A = np.array([2, 4, -6, 9])
B = np.array([3, -4, 2, 2])
print(A + B, A - B, A * B, A / B)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), np.divide(A, B))
print("^^^^^^^^^^^^^^^")
print(A + 3, B * 2, A + 2 * B)
# above "multiply" operation is multiplying each element of one array by corresponding element of the second array - ...
# ... this isn't matrix multiplication from linear algebra


################### MATRIX MULTIPLICATION - LINEAR ALGEBRA ##############

A = np.array(
    [[3, 5],
     [2, 4]]
)


B = np.array(
    [[1, 4],
     [0, 4]]
)

C = np.dot(A, B) # This is a matrix multiplication - according to linear algebra

print(A * B, "\n")
print(C, "\n")

print(A.dot(B), "\n")

print(A @ B) # "@" sign the same as  "np.dot()" operation

################### pseudo-random number generator (PRNG)####################

np.random.seed(0) # "seed" method set a seed of pseudo-random number generator

a = np.random.randn() # "randn" function from "random" module generates a value from NORMAL/GAUSSIAN DISTRIBUTION
print(a, '\n')

b = np.random.randn(10)
print(b, "\n")

c = np.random.randn(10, 3)
print(c, "\n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

z = np.random.rand(4, 6)  # "rand" function from "random" module generates a value from UNIFORM/RECTANGULAR DISTRIBUTION
# rozklad jednostajny) on interval (przedzial) <0,1>
print(z, "\n")

x = np.random.randint(low=10, high=101, size=15) # "randint" function generates a values from interval <low, high> and..
# .. "size" attribute is using to choose amount of generated values
print(x, "\n")

print(np.random.choice(x))  # "choice" function chose one value from LIST
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

data = np.arange(10)
print(data, "\n")
np.random.shuffle(data)  # "shuffle" function is use to shuffling (przetasowanie/przestawienie) a data form for...
#  example list
print(data)


######################## Basic functions in NumPy ########################3

print(np.exp(1), "\n") # exponential function
print(np.sqrt(9), "\n")

print(np.all([1, 2, 3]))  # "all" function checks do every elements of list are logical TRUE
print(np.all([1, 2, 0]), "\n")

print(np.any([1, 0, 0]))  # "any" function checks do ANY elements of list are logical TRUE
print(np.any([0, 0, 0]), "\n")
print("^^^^^^^^^^^^^^^^")

A = np.random.rand(5)
print(A)
print(np.argmax(A))  # "argmax" function get a INDEX the bigest value from list in argument this function
print(A[np.argmax(A)])  # In this way could get value the bigest element from list

print(np.argmin(A), "\n")  # "argmin" function get a INDEX the smallest value from list in argument this function

print(np.argsort(A), "\n")  # "argsort" functions sort indexs of element from list

print(np.max(A), "\n")

print(np.min(A), "\n")

print(np.mean(A), "\n")  # average of list elements

print(np.median(A), "\n")  # median of elements

print(np.std(A), "\n")  # standard deviation


##################### indexing and cutting elements from matrix #################

A = np.arange(15)
print(A, "\n")
A = A.reshape(5, 3)
print(A, "\n")

print(A[1], "\n")  # getting second row of matrix

print(A[:, -1], "\n")  # getting last column of matrix

print(A[1, 2], "\n")  # getting element from matrix which is in second row and third column

A[1, 2] = 10  # assign new value to element with index [1,2]
print(A)


################ ITERATING through ARRAY/MATRIX #############

A = np.arange(15)
print(A, "\n")
A = A.reshape(5, 3)
print(A, "\n")

for row in A:  # iterating through rows
    print(row)
print("\n")

for row in A:  # iterating through elements from first column
    print(row[0])
print("\n")

for item in A.flat:  # iterating through each element of matrix
    print(item)


############# CHANGE A SIZE OF MATRIX/ARRAY ##########33

A = np.arange(15)
print(A, "\n")
A = A.reshape(5, 3)
print(A, "\n")

print(A.reshape(3, 5), "\n")  # change size matrix A from [5,3] to [3,5]

print(A.T)  # transposition A matrix
"""

############### LOGICAL MASKS ################

A = np.arange(start=-10, stop=10, step=0.5)
print(A, "\n")

A = A.reshape(10, -1)
print(A, "\n")

print(A > 0, "\n")  # equation in print function checks which elements from array A are bigger than 0 - we get a LOGICAL...
# ...MASK (array with TRUE where element is bigger than 0 and FALSE where element is less than 0)

B = A[A > 0]  # assigning to variable B every elements from A array wich is bigger than 0
print(B, "\n")

print(np.bitwise_and(A > -5, A < 5), "\n")  # "bitwise_and" function is used to creating LOGICAL MASK with two logical..
# .. condition - logical AND

C = A[np.bitwise_and(A > -5, A < 5)]
print(C)
