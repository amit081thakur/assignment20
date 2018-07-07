import numpy


#Question -1

array1 = numpy.arange(10).reshape(10,1)
print(" array one : ")
print(array1)
print(" Mean of array one  is ",numpy.mean(array1))

array2 =  (2 * numpy.random.rand(10,1) + 1.3)
print("array two ",array2)
print(" Mean of array two is {}",numpy.mean(array2, dtype=numpy.int8))



#Question -2

array3 =  numpy.random.rand(20,1).reshape(4,5)
print("array three",array3)
print("Standard Deviation =",numpy.std(array3, dtype=numpy.float64))


array4 =  numpy.random.rand(20,1).reshape(5,4)
print("array4 ",array4)
print("Mean = {}",numpy.mean(array4, dtype=numpy.float32))



#Question -3

matrix1 = (1 * numpy.random.rand(10,20) + 1)
print("matrix one>>>>",matrix1)

matrix2 = 1 * numpy.random.rand(20,25) +1
print("matrix two>>>>",matrix2)

matrix3 = matrix1.dot(matrix2)
print("multiplication of matrix>>>")
print(matrix3)

print("sum of matrices>>>>",numpy.sum(matrix3))



#Question -4

def func(x):
    x = 1 / (1 + numpy.exp(-x))
    return x

ar1 = numpy.arange(10).reshape(10,1)
print(ar1)

for we in ar1:
    arrr= func(we)
    numpy.asanyarray(arrr)

print("array : ",arrr)