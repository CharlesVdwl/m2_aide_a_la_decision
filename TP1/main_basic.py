#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	Main to give example evaluation function
"""
from solution import *
from graphProblem import *


def main():
	#----------------
	# Parameters

	# number of nodes
	n = 19

	#----------------
	# Declaration

	# Evaluation function
	problem = GraphProblem()

	# One solution with n nodes
	solution = Solution(n)

	#----------------
	# Execute

	solution.random_graph(0.18)
	# solution.add_edge(0, 2)
	# solution.add_edge(0, 3)
	# solution.add_edge(0, 4)
	# solution.add_edge(1, 4)
	# solution.add_edge(1, 5)

	# solution.add_edge(2, 4)

	# solution.add_edge(2, 3)
	# solution.remove_edge(2, 3)
	# i = solution.index_bit(2, 3)
	# #print(i)
	# solution.set_bit(i, True)

	# solution.add_edge(3, 4)
	# solution.add_edge(3, 5)

	problem.eval(solution)

	print(solution)

	# Save into png file
	solution.draw("graph_res/alea.png")

	# Matrice d'adjacence
	#print(nx.adjacency_matrix(solution.G).todense())
	#voisin = nx.adjacency_matrix(solution.G).todense()
	#print(voisin)
	#voisin[2][5] = not voisin[2][5]
	#print(voisin)

if __name__ == '__main__':
	main()

