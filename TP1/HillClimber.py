from solution import *
from graphProblem import *
import random as rdm
import time

def Hill_Climber(node_nbr, it_nbr, s=None):

    begin = time.time()

    problem = GraphProblem()

    # solution initiale
    if s :
        solution = s
    else :
        solution = Solution(node_nbr)
        solution.random_graph(0.15)
        problem.eval(solution)

    f_best = solution.fitness

    # hill-climb
    it = 0
    best = True
    while it < it_nbr and best :

        best = False
        i_best = -1
        j_best = -1
        for i in range(node_nbr):
            for j in range(i, node_nbr) :
        
                # voisin
                solution.flip_edge(i, j)

                # meilleur ?
                problem.eval(solution)
                if f_best > solution.fitness :
                    i_best = i
                    j_best = j
                    f_best = solution.fitness
                    best = True

                # retour à la solution de base
                solution.flip_edge(i, j)

        if best :
            solution.flip_edge(i_best, j_best)

        it += 1

    problem.eval(solution)
    return (solution, it, time.time()-begin)

# s, pas, tps = Hill_Climber(19, 30)
# print(s)
# s.draw("graph_res/hill_climber.png")
# print(nx.adjacency_matrix(s.G).todense())
# print(pas)
# print(tps)