import networkx as nx

def shortest_way(g, x, y):
    path = nx.dijkstra_path(g, x, y)
    length = nx.dijkstra_path_length(g, x, y)
    return path, length


city_pair = []
cities = []
array = list(open('cities.csv'))
for i in array:
    a, b, c = i.split(';')
    city_pair = [a, b, int(c)]
    cities.append(city_pair)
print(cities)

graph = nx.Graph()
graph.add_weighted_edges_from(cities)

source = (input('Enter starting point: ')).replace(' ', '').capitalize()
target = (input('Enter destination: ')).replace(' ', '').capitalize()
print(shortest_way(graph, source, target))


