import heapq

def ucs(graph, start, end, cost):
    closeList = []
    openList = [(0, start)]  # Priority queue with (cost, node)
    data = []
    parent = {start: None}  # To track the path
    cost_so_far = {start: 0}  # Cost to reach each node

    def successor(node):
        return graph[node]

    def GT(node):
        return node == end

    done = False
    while openList and not done:
        current_cost, top = heapq.heappop(openList)  # Get node with lowest cost
        data.append([openList.copy(), top, closeList.copy(), GT(top), successor(top)])
        closeList.append(top)

        if GT(top):
            done = True
            break

        for x in successor(top):
            new_cost = current_cost + cost[(top, x)]
            if x not in cost_so_far or new_cost < cost_so_far[x]:
                cost_so_far[x] = new_cost
                heapq.heappush(openList, (new_cost, x))
                parent[x] = top  # Track the parent of each node

    # Print the data in a readable format
    print("openList\tNode\tcloseList\tGT(Node)\tSuccessor(Node)")
    for entry in data:
        openList, node, closeList, GT_node, successor_node = entry
        print(f"{openList}\t{node}\t{closeList}\t{GT_node}\t{successor_node}")

    return data, parent

def findPath(parent, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()  # Reverse to get the path from start to end
    return path

# Example adjacency list with costs
adjacencyList = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'A'],
    'C': ['B'],
    'D': ['A', 'E', 'I', 'H'],
    'E': ['B', 'F', 'I', 'D'],
    'F': ['G', 'E'],
    'H': ['D', 'I'],
    'I': ['E', 'G', 'H', 'D'],
    'G': ['F', 'I', 'E'],
}

# Example costs associated with each edge
cost = {
    ('A', 'B'): 1,
    ('A', 'D'): 4,
    ('B', 'C'): 2,
    ('B', 'E'): 5,
    ('B', 'A'): 1,
    ('C', 'B'): 2,
    ('D', 'A'): 4,
    ('D', 'E'): 1,
    ('D', 'I'): 2,
    ('D', 'H'): 3,
    ('E', 'B'): 5,
    ('E', 'F'): 1,
    ('E', 'I'): 2,
    ('E', 'D'): 1,
    ('F', 'G'): 3,
    ('F', 'E'): 1,
    ('H', 'D'): 3,
    ('H', 'I'): 1,
    ('I', 'E'): 2,
    ('I', 'G'): 1,
    ('I', 'H'): 1,
    ('I', 'D'): 2,
    ('G', 'F'): 3,
    ('G', 'I'): 1,
    ('G', 'E'): 4,
}

start = 'A'
end = 'G'
data, parent = ucs(adjacencyList, start, end, cost)
path = findPath(parent, start, end)
print("\nPath: " + " -> ".join(path))
