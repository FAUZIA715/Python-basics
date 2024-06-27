def prim(graph):
    """
    Find the minimum cost spanning tree of an undirected graph
    using Prim's algorithm.

    Args:
    graph (dict): A dictionary representing the graph. Each key
        is a node label and the corresponding value is a list of
        tuples representing the edges emanating from that node.
        Each tuple contains the label of the adjacent node and the
        cost of the edge.

    Returns:
    A dictionary representing the minimum cost spanning tree. Each
    key is a node label and the corresponding value is a list of
    tuples representing the edges emanating from that node in the
    minimum cost spanning tree. Each tuple contains the label of the
    adjacent node and the cost of the edge.
    """
    mst = {}  # initialize the minimum cost spanning tree
    visited = set()  # initialize the set of visited nodes
    start_node = list(graph.keys())[0]  # start from the first node in the graph
    edges = [(cost, start_node, adj_node) for adj_node, cost in graph[start_node]]
    visited.add(start_node)  # mark the start node as visited
    while edges:
        # find the edge with the minimum cost
        min_cost, src, dest = min(edges)
        edges.remove((min_cost, src, dest))
        if dest in visited:  # check for cycles
            continue
        visited.add(dest)  # mark the destination node as visited
        if src in mst:
            mst[src].append((dest, min_cost))
        else:
            mst[src] = [(dest, min_cost)]
        for adj_node, adj_cost in graph[dest]:
            if adj_node not in visited:
                edges.append((adj_cost, dest, adj_node))
    return mst


# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 5)],
    'D': [('B', 1), ('C', 5)]
}

mst = prim(graph)

print("Minimum cost spanning tree:")
for node, edges in mst.items():
    for dest, cost in edges:
        print(f"{node} --{cost}-- {dest}")
