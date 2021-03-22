from matplotlib import pyplot as plt 
from view.two_dimension_script import graph_functions

#Se grafican las restricciones 
x = range(0, 20)

#Restricción 1
f1 = lambda x:20 - 2*x
f2 = lambda x: 16 - x 

graph_functions(f1, f2, x)
