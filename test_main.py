from main import *

def test_shortest_shortest_path():
    graph = {
        's': {('a', 1), ('c', 4)},
        'a': {('b', 2)},
        'b': {('c', 1), ('d', 4)},
        'c': {('d', 3)},
        'd': {},
        'e': {('d', 0)}
    }
    distances, edge_counts = shortest_shortest_path(graph, 's')
    assert distances['s'] == 0
    assert edge_counts['s'] == 0
  # result has both the weight and number of edges in the shortest shortest path
    

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'


def test_get_path():
  graph = get_sample_graph()
  parents = bfs_path(graph, 's')
  assert get_path(parents, 'd') == 's->b->c->d'
