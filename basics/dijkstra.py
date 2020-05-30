def main():
    G = read_graph()
    if __debug__: print(G)
    start = input("Vertex to begin:")
    while start not in G:
        start = input("No such vertex in the graph. " +
                "Enter vertex to begin:")
    shortest_distances = dijkstra(G, start)
    finish = input("Vertex to route to:")
        
    while start not in G:
        start = input("No such vertex in the graph. " +
                "Enter vertex to begin:")
    shortest_path = restore_shortest_path(G, start, finish,
            shortest_distances)

def read_graph():
    edge_num = int(input())
    graph = {}
    for i in range(edge_num):
        vertex_a, vertex_b, weight = input().split()
        weight = float(weight)
        add_edge(graph, vertex_a, vertex_b, weight)
        add_edge(graph, vertex_b, vertex_a, weight)

    return graph

def add_edge(graph, vertex_a, vertex_b, weight):
    if vertex_a not in graph:
        graph[vertex_a] = {vertex_b: weight}
    else:
        graph[vertex_a][vertex_b] = weight

def restore_shortest_path(graph, vertex_from, vertex_to, distance_value):
    pass

def dijkstra(graph, start_vertex):
    #distances = [INF] * vertex_num
    pass

if __name__ == "__main__":
    main()

