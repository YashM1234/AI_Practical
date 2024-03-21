#Aim: Write a simple python program to implement Breadth first search algorithm (Heuristic search) to    calculate the sequence of set of visited node in AI.
def BFS(graph,start,dest) -> list():
    queue = list()
    visited = list()
    queue.append(start)
    print('Visited',start)
    result = ["Not reachable",list()]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node==dest:
            print('Destination node found',node)
            result[0] = 'Reachable'
            break
        print(node,'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
    result[1] = visited
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['H'],
    'H': []
}
result = BFS(graph, "A", "E")
print(result[0])
print("Path used to traverse :-" , result[1])