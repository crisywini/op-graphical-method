import sympy as sym

def get_solutions(functions_list:list, Z, max:bool, restrictions_bool:list) -> (int, int, int):
    '''
    This method allows to get the solutions based on the restrictions and the type
    if is the minimun then the max should be False, True otherwise
    '''
    #Find intersections
    possible_solutions = []
    solutions = get_intersections(functions_list)
    for s in solutions:
        keys = list(s[0].keys())
        x = s[0][keys[0]]
        y = s[0][keys[1]]
        possible_solution = Z(x, y)
        possible_solutions.append((x, y, possible_solution))
    #Encontrar dependiendo de la función, si es maximo entonces mayor z, 
    #si es mínimo entonces menor z
    x, y, z = 0, 0, 0
    if max:
        x, y, z = find_max(possible_solutions, restrictions_bool)
    else:
        x, y, z = find_min(possible_solutions, restrictions_bool)


    #Evaluate in the function
    return x, y, z
def get_intersections(functions_list:list) -> list:
    '''
    This method allows to get the intersections in the restrictions 
    '''
    solutions = []
    for f in functions_list:
        for f2 in functions_list:
            if f != f2:
                resp = sym.solve([f, f2], dict=True)
                if len(resp)>0:
                    solutions.append(resp)
    return solutions

def find_max(possible_solutions:list, restrictions_bool:list) -> (int, int, int):
    '''
    This method allows to get maximum when is needed
    '''
    max_ = -1
    x, y = 0,0
    for i in range(0, len(possible_solutions)):
        list_test = [restrictions_bool[j](possible_solutions[i][0],possible_solutions[i][1]) for j in range(0, len(restrictions_bool))]
        if max_ < possible_solutions[i][2] and False not in list_test:
            max_ = possible_solutions[i][2]
            x = possible_solutions[i][0]
            y = possible_solutions[i][1]
    return x, y, max_

def find_min(possible_solutions:list, restrictions_bool:list) -> (int, int, int):
    '''

    '''
    min_ = 10000000
    x, y = 0,0
    for i in range(0, len(possible_solutions)):
        list_test = [restrictions_bool[j](possible_solutions[i][0],possible_solutions[i][1]) for j in range(0, len(restrictions_bool))]
        if min_ > possible_solutions[i][2] and False not in list_test:
            min_ = possible_solutions[i][2]
            x = possible_solutions[i][0]
            y = possible_solutions[i][1]
    return x, y, min_

x = sym.Symbol('x')
y = sym.Symbol('y')
restrictions = [x + y-30, x-15, y-18]
restrictions_bool = [(lambda x, y: x + y <= 30), (lambda x, y: x <= 15), (lambda x, y: x <= 18), (lambda x, y: x>=0 and y>=0)]
Z = lambda x, y: 40*x + 38*y

x, y, z = get_solutions(restrictions, Z, True, restrictions_bool)

print('x: '+str(x), 'y: '+str(y), 'z: '+str(z))

#resp = sym.solve([2*x+y-18, x-6], dict=True)
#print(resp)
#keys = list(resp[0].keys())
#print(keys)
#print(resp[0][keys[0]], resp[0][keys[1]])
