import networkx as nx
import matplotlib.pyplot as plt

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
print(graph)

nx.draw(graph, with_labels=True)
plt.savefig("cities.png")
