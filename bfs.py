def bfs(graph, start, end):
    closeList = []
    openList = [start]
    data = []
    parent = {start: None}  # To track the path

    def successor(node):
        return graph[node]

    def GT(node):
        return node == end

    done = False
    while openList and not done:
        top = openList.pop(0)
        data.append([openList.copy(), top, closeList.copy(), GT(top), successor(top)])
        closeList.append(top)
        
        if GT(top):
            done = True
            break

        for x in successor(top):
            if x not in closeList and x not in openList:
                openList.append(x)
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

# Example adjacency list
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

start = 'A'
end = 'G'
data, parent = bfs(adjacencyList, start, end)
path = findPath(parent, start, end)
print("\nPath: " + " -> ".join(path))
