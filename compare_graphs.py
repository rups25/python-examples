import subprocess

class Vertex:
  def __init__(self, data):
    self.data = data
    self.neighbors = []

def draw_graph(g, graph_file_name):
    graph_model = ''
    for vertex in g:
        for neighbor in vertex.neighbors:
            graph_model += ' %s -- %s;' % (vertex.data, neighbor.data)
    graph_model = 'graph G {%s}' % graph_model
    cmd = 'echo "%s" | dot -T png > %s' % (graph_model, graph_file_name)
    return_code = subprocess.call(cmd, shell=True)

def compare_graphs(graph1, graph2):
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

def build_test_graph_alpha():
  graph_alpha = [Vertex(i) for i in xrange(4)]
  graph_alpha[0].neighbors.append(graph_alpha[1])
  graph_alpha[1].neighbors.append(graph_alpha[0])
  graph_alpha[1].neighbors.append(graph_alpha[2])
  graph_alpha[2].neighbors.append(graph_alpha[1])
  graph_alpha[2].neighbors.append(graph_alpha[3])
  graph_alpha[3].neighbors.append(graph_alpha[2])
  return graph_alpha

def build_test_graph_beta():
  graph_beta = [Vertex(i) for i in xrange(4)]
  graph_beta[0].neighbors.append(graph_beta[1])
  graph_beta[1].neighbors.append(graph_beta[0])
  graph_beta[1].neighbors.append(graph_beta[2])
  graph_beta[2].neighbors.append(graph_beta[1])
  graph_beta[1].neighbors.append(graph_beta[3])
  graph_beta[3].neighbors.append(graph_beta[1])
  return graph_beta

def main():
    graph1 = build_test_graph_alpha()
    graph2 = build_test_graph_beta()

    # Draw the graphs
    draw_graph(graph1, 'graph1.png')
    draw_graph(graph2, 'graph2.png')

    # Compare the graphs
    print(compare_graphs(graph1, graph2))

if __name__ == '__main__':
    main()
