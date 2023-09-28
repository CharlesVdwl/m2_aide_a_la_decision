from solution import *
from graphProblem import *
import random as rdm
from HillClimber import Hill_Climber
import time
import numpy as np
import math

def ILS(node_nbr, it_nbr, it_nb_algo, perturbation) :

    begin = time.time()

    problem = GraphProblem()

    taille = (node_nbr*(node_nbr-1))/2
    solution, _, _ = Hill_Climber(node_nbr, it_nb_algo)

    solutionF = solution.copy(Solution(node_nbr))

    for i in range(it_nbr):
        print(i+1)
            # perturbation
        for _ in range(floor(perturbation * taille)) :
            ind = rdm.randint(0, taille-1)
            solution.flip_bit(ind)

        problem.eval(solution)
        solution2, _, _ = Hill_Climber(node_nbr, it_nb_algo, solution)

        if solution2.fitness < solutionF.fitness :
            solution2.copy(solution)
            solution2.copy(solutionF)

    return solutionF, time.time()-begin

sol, tps = ILS(19, 10, 45, 0.15)
print(sol)
sol.draw("graph_res/ILS.png")
# print(nx.adjacency_matrix(sol.G).todense())
# print(tps)