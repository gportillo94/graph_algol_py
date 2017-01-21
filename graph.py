import random 
import time

def createAjdList(numberVertex):
	"""
		Crea la lista de adyacencias de un grafo
		con un numero de vertices dado.
		regresa una Lista de Conjuntos
	"""
	#numberVertex = int(random.uniform(1,20))
	#numberVertex = 5
	#numInciden = int(numberVertex/10)+1
	adjList = []
	for i in range(numberVertex):
		adjList.append(set())
	for i in range(numberVertex):
		for j in range (int(random.uniform(0,(numberVertex-1)/8))):
			newEdge = int(random.uniform(0,numberVertex)) 
			adjList[i].add(newEdge)
			adjList[newEdge].add(i)
	return adjList

def BFS (adjList, vertex):
	level = {vertex:0}
	parent = {vertex:None}
	i = 1
	frontier = [vertex]
	while frontier: 
		nextVer = []
		for u in frontier:
			for v in adjList[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					nextVer.append(v)
		#print(nextVer)
		frontier = nextVer
		i = i+1
	print(level)
	print("Parent")	
	print(parent)

def DFS(adjList, vertex):
	"""
		Visita todos los vertices alcanzables desde 'vertex'
		Visitara todos los nodos de un grafo si y solo si el grafo es conectado
	"""
	parent = {vertex:None}
	def DFS_visit(vertex):
		for v in adjList[vertex]:
			if v not in parent:
				parent[v] = vertex
				DFS_visit(v)
	DFS_visit(vertex)
	print(parent)

def complete_DFS(adjList):

	parent = {}
	def DFS_visit(vertex):
		for v in adjList[vertex]:
			if v not in parent:
				parent[v] = vertex
				DFS_visit(v)

	for s in range(len(adjList)):
		if s not in parent:
			parent[s] = None
			DFS_visit(s)
	print(parent)

def printGraph (adjList):
	for i,j in enumerate(adjList):
		print(i,adjList[i])

def main():
	
	#now = time.time()
	adjList = createAjdList(25)
	#print(time.time() - now)
	printGraph(adjList)
	now = time.time()
	BFS(adjList,0)
	#print(time.time() - now)
	#DFS(adjList,0)
	#complete_DFS(adjList)

if __name__ == '__main__':
	main()