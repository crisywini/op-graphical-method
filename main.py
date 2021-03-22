from matplotlib import pyplot as plt 
from view.two_dimension_script import graph_functions_

#Se grafican las restricciones 
x = range(0, 130)

#Restricción 1
f1 = lambda x: 20*x - 2300
f2 = lambda x: 30*x - 1540 
f3 = lambda x: (2440 - 25*x)/23
f4 = lambda x: (1300 - 11*x)/11 


graph_functions_(f1, f2, f3, f4, x)
