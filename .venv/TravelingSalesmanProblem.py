#Aim: Traveling salesman problem
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem

def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path

# Driver Code
if __name__ == "__main__":
    graph = []
    x = int(input("Enter the number of cities: "))
    x = x+1  # Here we increment x by 1 to get the correct output order
    for i in range(1, x):
        y = []
        for j in range(1, x):
            print("Enter the distance between cities {0}-{1}: ".format(i, j))
            temp = int(input())
            y.append(temp)
        graph.append(y)
    s = 0
    print("The Minimum cost is ", travellingSalesmanProblem(graph, s))
