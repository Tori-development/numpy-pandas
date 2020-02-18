
import numpy as np
b = np.ones((2,2))
print(b)

#2.	Devolver dimension/forma del arreglo
b = np.array([[1,2],[4,5]])
print(b.shape)

#3.	Crear un arreglo de 100x100x100 lleno de 0s
b = np.zeros((100,100,100))
print(b)

#4.	Crear una matriz identidad de 5x5
b = np.eye(5)
print(b)

#5.	Crear un arreglo de dimension 42x42 lleno de 42
b = np.full((42,42), 42)
print(b)

#6.	Crear un arreglo de 3x3 con valores random
b = np.random.random((3,3))
print(b)

#6.	Crear arreglo de 5x4 con valores del 1-20
x = np.arange(21)
val1 = x[1:5]
val2 = x[5:9]
val3 = x[9:13]
val4 = x[13:17]
val5 = x[17:21]

array1 = np.array([val1,val2,val3,val4,val5])
print(array1)

#Llenar un arreglo de 3x3 de los valores q corresponden
#de la fila 3,4 y 5 y la de la columna 1,2,3

array2 = np.array([val3[0:3],val4[0:3],val5[0:3]])
print(array2)

#Crear un arreglo con la misma forma que el anterior ¿?

array3 = np.empty_like(array2)
for i in range(3):
    array3[i,:]=array2[i,:]+1
print("array3", array3)


#7. Crear arreglo de 5x4 con valores del 1-20

array = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]])

print(array[[0, 1, 2], [0, 1, 0]])