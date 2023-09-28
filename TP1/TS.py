from solution import *
from graphProblem import *
import random as rdm
import math

def Tabou(node_nbr, it):

    T = []
    solution = Solution(node_nbr)
    solution.random_graph(0.1)
    problem = GraphProblem()
    problem.eval(solution)

    for _ in range(it):
        
        i_best = -1
        j_best = -1
        f_best = 99999
        for i in range(node_nbr):
            for j in range(i, node_nbr) :
        
                if (i, j) not in T :
                    # voisin
                    solution.flip_edge(i, j)

                    # meilleur ?
                    problem.eval(solution)
                    if f_best > solution.fitness :
                        i_best = i
                        j_best = j
                        f_best = solution.fitness

                    # retour à la solution de base
                    solution.flip_edge(i, j)

        problem.eval(solution)
        if f_best < solution.fitness :
            solution.flip_edge(i_best, j_best)

        T.append((i_best, j_best))

    problem.eval(solution)
    return solution

   
    
s = Tabou(19, 100)
print(s)
s.draw("graph_res/tabou.png")