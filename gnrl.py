from math import *
from pulp import *
import numpy as np

#nombre d'arcs et nombre de sommets
n = int(input('entrer le nombre de sommets n= '))
m = int(input('entrer le nombres des arcs m= '))

#la matrice d'incidence
print('entez la matrice d\'incidence :')
x = [[int(input()) for j in range(m)] for i in range(n)]
print('la matrice d\'incidence est x=', x)

#les capacités
print('entez les capacités max :')
c = [int(input()) for j in range(m)]
print('le vecteur capacité max est c= ', c)

print('entrez les capacités min:')
b = [int(input()) for j in range(m)]
print('le vecteur capacité min est b= ', b)

#fct matrice
cost_matrix = [0 for j in range(m)]
cost_matrix[m-1] = 1

#initialiser la classe de pl
prob = LpProblem("maximum flow", LpMaximize)

#definir les variables de decision
variables_indices = [str(i) for i in range(1, m+1)]
variables_indices.sort()
DV_variables = LpVariable.matrix("f", variables_indices, cat="Integer", lowBound=0)
flow = np.array(DV_variables).reshape(m)
print("les variables de décision sont : ", flow)

#la fonction objectif
obj_func = lpSum(flow*cost_matrix)
print('la fonction objectif est Z(Max) = ', obj_func)
prob += obj_func

#les contraintes de capacités min
print('les contraintes de capacités min sont :')
for i in range(m-1):
    print(b[i] <= flow[i])
    prob += b[i] <= flow[i], "les contraintes de capacités min" + str(i)

#les contraintes de capacités max
print('les contraintes de capacités max sont :')
for i in range(m-1):
    print(flow[i] <= c[i])
    prob += flow[i] <= c[i], "les contraintes de capacités max" + str(i)

# la contrainte E*f
print('les contraintes la somme de E*f sont : ')
for i in range(n):
    print(lpSum(x[i][j]*flow[j] for j in range(m)) == 0)
    prob += lpSum(x[i][j]*flow[j] for j in range(m)) == 0, "Demand Constraints " + str(i)
print(prob)

#la solutio du problème
prob.solve(PULP_CBC_CMD(msg=0))

status = LpStatus[prob.status]

print(status)
print("la valeur de flot max est :", prob.objective.value())

# Decision Variables

for v in prob.variables():
    try:
        print(v.name, "=", v.value())
    except:
        print("error couldnt find value")
