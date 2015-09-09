class Vertex:
  def __init__(self, data):
    self.data = data
    self.neighbors = []


def compare_graphs():
  graph1 = [Vertex(i) for i in xrange(4)]
  graph1[0].neighbors.append(graph1[1])
  graph1[1].neighbors.append(graph1[0])
  graph1[1].neighbors.append(graph1[2])
  graph1[2].neighbors.append(graph1[1])
  graph1[2].neighbors.append(graph1[3])
  graph1[3].neighbors.append(graph1[2])
   
  graph2 = [Vertex(i) for i in xrange(4)]
  graph2[0].neighbors.append(graph2[1])
  graph2[1].neighbors.append(graph2[0])
  graph2[1].neighbors.append(graph2[2])
  graph2[2].neighbors.append(graph2[1])
  graph2[2].neighbors.append(graph2[3])
  graph2[3].neighbors.append(graph2[2])
  
  graph1_num_neighbors = {}
  graph2_num_neighbors = {}
  
  for vertex in graph1:
    length_of_neighbors = len(vertex.neighbors)
    if length_of_neighbors not in graph1_num_neighbors:
      graph1_num_neighbors[length_of_neighbors] = [vertex]
    else:
      graph1_num_neighbors[length_of_neighbors].append(vertex)
  
  for vertex in graph2:
    length_of_neighbors = len(vertex.neighbors)
    if length_of_neighbors not in graph2_num_neighbors:
      graph2_num_neighbors[length_of_neighbors] = [vertex]
    else:
      graph2_num_neighbors[length_of_neighbors].append(vertex)
  
    
compare_graphs()
    
  

  
  

