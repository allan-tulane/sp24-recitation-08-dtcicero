from collections import deque
import heapq
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    distance = {vertex: float('inf') for vertex in graph}
    edge_count = {vertex: float('inf') for vertex in graph}
    distance[source] = 0
    edge_count[source] = 0

    
    pq = [(0, 0, source)]  

    
    while pq:
        dist, edge_cnt, current = heapq.heappop(pq)
        if dist > distance[current]:
            continue
        for neighbor, weight in graph[current]:
            new_dist = dist + weight
            new_edge_cnt = edge_cnt + 1
            if new_dist < distance[neighbor] or (new_dist == distance[neighbor] and new_edge_cnt < edge_count[neighbor]):
                distance[neighbor] = new_dist
                edge_count[neighbor] = new_edge_cnt
                heapq.heappush(pq, (new_dist, new_edge_cnt, neighbor))

    
    return distance, edge_count
    

    
    
def bfs_path(graph, source):
  parent = {} 

 
  queue = deque([source])

 
  parent[source] = None

  
  while queue:
    current = queue.popleft()
    for neighbor in graph[current]:  
          if neighbor not in parent:
              parent[neighbor] = current
              queue.append(neighbor)

  return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  path = []
  current = destination
  while current is not None:
      path.append(current)
      current = parents[current]  

  path.reverse()

  path_str = '->'.join(path)

  return path_str

