from solution import *
from graphProblem import *
import random as rdm
import math

def Recuit(node_nbr, it):

    solution = Solution(node_nbr)
    solution.random_graph(0.1)
    problem = GraphProblem()
    problem.eval(solution)

    k = 1

    for i in range(it):
        fit = solution.fitness

            # voisin
        e1 = rdm.randint(0, node_nbr-1)
        e2 = rdm.randint(0, node_nbr-1)
        while e2 == e1 :
            e2 = rdm.randint(0, node_nbr-1)
        solution.flip_edge(e1, e2)

            # fitness nouvelle solution
        problem.eval(solution)

            # recuit
        if solution.fitness >= fit :
            if math.exp((solution.fitness-fit)/k) > rdm.random() :
                solution.flip_edge(e1, e2)
                solution.fitness = fit

        k = k+1

    return solution

    
s = Recuit(19, 20000)
print(s)
s.draw("graph_res/recuit.png")