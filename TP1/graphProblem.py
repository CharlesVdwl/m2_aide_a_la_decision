import networkx as nx
import numpy as np
from math import sqrt
from solution import *

class GraphProblem:
	def __init__(self, penaltyWeight = 100):
		self.defaultValue = 99999
		self.penaltyWeight  = penaltyWeight

	def eval(self, solution):
		solution.n_cc = 0
		solution.largest_cc = 0
		gc_max = None

		size_ccs = 0
		for c in nx.connected_components(solution.G):
			solution.n_cc += 1
			size_ccs += len(c)
			if len(c) > solution.largest_cc:
				solution.largest_cc = len(c)
				gc_max = solution.G.subgraph(c) # I hope there is no expensive operation, only pointer?

		solution.n_cc += solution.n - size_ccs # to add single nodes which are not in the connected components

		
		if solution.largest_cc > 1:
			# vp = nx.adjacency_spectrum(gc_max)
			# radius = -1
			# for z in vp:
			# 	if z.imag == 0: # only a check, supposed to be zero
			# 		radius = max(radius, abs(z.real))
			evals = np.linalg.eigvalsh(nx.adjacency_matrix(solution.G).todense())
			evalsRealAbs = np.zeros_like(evals)
			for i in range(len(evals)) :
				evalsRealAbs[i] = abs(evals[i])
			lambda1 = max(evalsRealAbs)

			mu = len(nx.max_weight_matching(gc_max))

			solution.fitness = lambda1 + mu - sqrt(solution.largest_cc - 1) + 1

			# penalty if there is several connected components
			solution.fitness += self.penaltyWeight * (solution.n_cc - 1)
		else:
			solution.fitness = self.defaultValue
