import networkx as nx
import matplotlib.pyplot as plt
import copy
from math import sqrt, floor

class Solution:
	def __init__(self, n):
		# number of nodes
		self.n = n

		# non directed graph 
		self.G = nx.Graph()

		# graph with n nodes without edges
		self.G.add_nodes_from(list(range(self.n)))

		# number of connected components
		self.n_cc = n

		# size of the largest connected component
		self.largest_cc = 1

		# fitness value
		self.fitness = None

	def random_graph(self, p):
		self.G = nx.erdos_renyi_graph(self.n, p)

	"""
	generate neighbors by k distance of the solution
	"""
	def generate_neighbors(self, k, neighbors=[], first=True):

		if first :
			neighbors = [self]
		new_neighbors = []

		for n in neighbors :
			for i in range(self.n):
				for j in range(i, self.n):
					neighbor = copy.deepcopy(n)
					neighbor.flip_edge(i, j)
					new_neighbors.append(neighbor)

		if k <= 1 :
			#print(len(new_neighbors))
			return new_neighbors
		else:
			return self.generate_neighbors(k-1, new_neighbors, first=False)


	"""
		Add one edge between nodes i and j, and set the corresponding bit
	"""
	def add_edge(self, node_i, node_j):
		self.G.add_edge(node_i, node_j)
		self.fitness = None

	"""
		Remove one edge between nodes i and j, and set the corresponding bit
	"""
	def remove_edge(self, node_i, node_j):
		self.G.remove_edge(node_i, node_j)
		self.fitness = None

	"""
		Flip one edge between nodes i and j (add or remove)
	"""
	def flip_edge(self, node_i, node_j):
		if self.G.has_edge(node_i, node_j):
			self.remove_edge(node_i, node_j)
		else:
			self.add_edge(node_i, node_j)

		self.fitness = None

	"""
		Flip the value of bit i, and the corresponding edge
	"""
	def flip_bit(self, i):
		node_i, node_j = self.index_nodes(i)

		if self.G.has_edge(node_i, node_j):
			self.remove_edge(node_i, node_j)
		else:
			self.add_edge(node_i, node_j)

	"""
		Set the value of bit i, and the corresponding edge
	"""
	def set_bit(self, i, value):
		node_i, node_j = self.index_nodes(i)

		if value:
			if self.G.has_edge(node_i, node_j):
				self.remove_edge(node_i, node_j)
		else:
			if not self.G.has_edge(node_i, node_j):
				self.add_edge(node_i, node_j)

	"""
		Get the value of bit i, i.e. the corresponding edge
	"""
	def get_bit(self, i):
		node_i, node_j = self.index_nodes(i)

		return(self.G.has_edge(node_i, node_j))

	"""
		Index of the bit corresponding to the edge (node_i, node_j)
	"""
	def index_bit(self, node_i, node_j):
		return( int((2 * self.n - 1 - node_i) * node_i / 2 + (node_j - node_i - 1)) )

	"""
		Index (between 0 and n(n-1)/2-1) of the edge given by nodes index (node_i, node_j) for the corresponding bit
	"""
	def index_nodes(self, u):
		delta = ((2 * self.n - 1) / 2)**2 - 2 * u
		i = int(floor( (2 * self.n - 1) / 2 - sqrt(delta) ) )
		j = int(u - (2 * self.n - 1 - i) * i / 2 + i + 1)

		return(i, j)

	def clear(self):
		self.G.clear()
		self.fitness = None

	def copy(self, s):
		s.n = self.n
		s.G = self.G.copy()
		s.fitness = self.fitness
		s.n_cc = self.n_cc
		s.largest_cc = self.largest_cc

		return(s)

	def draw(self, filename):
		nx.draw(self.G, with_labels=True, font_weight='bold')
		plt.savefig(filename)

	def __str__(self):
		if self.G.number_of_nodes() != 0:
			str_A = "\""
			first = True
			for u, v in self.G.edges:
				if first:
					first = False
				else:
					str_A += ","
				str_A += "%d %d" % (u, v)
			str_A += "\""

			return(str(self.fitness) + " " + str(self.n) + " " + str_A)
		else:
			return(str(self.fitness) + " 0 []")
