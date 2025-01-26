class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[]*n for i in range(n)]
        print(self.adj)
    def createedge(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
        print(self.adj)
    def BFS(self, source):
        result = []
        queue = []
        visited = [False]*self.n

        distance = [-1]*self.n

        queue.append(source)
        visited[source] = True
        distance[source] = 0

        while len(queue) > 0:
            temp = queue.pop(0)
            result.append(temp)

            for node in self.adj[temp]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
                    distance[node] = distance[temp]+1
        #         print(visited)
        #         print(queue)
        # print(distance)
        return result

    def dfs_util(self, source, visited, result):
        result.append(source)
        visited[source] = True

        for node in self.adj[source]:
            if visited[node] == False:
                self.dfs_util(node, visited, result)
    
    def DFS(self, source):
        visited = [False]*self.n
        result = []
        self.dfs_util(source, visited, result)
        return result

graph = None

while True:
    print("Press 1 to create edge")
    print("Press 2 to print BFS")
    print("Press 3 to print DFS")
    print("Press 4 to exit")

    choice = int(input("Enter option: "))

    if choice == 1:
        amount = int(input("How many numbers would you like: "))
        graph = Graph(amount)
        for i in range(amount):
            x = int(input("What would you like the first number to be: "))
            y = int(input("What would you like the second number to be: "))
            graph.createedge(x, y)

    elif choice == 2:
        source = int(input("Which node would you like to start the search with: "))
        print(graph.BFS(source))

    elif choice == 3:
        source = int(input("Which node would you like to start the search with: "))
        print(graph.DFS(source))

    elif choice >= 4:
        break


# graph = Graph(5)
# graph.createedge(1, 5)
# graph.createedge(5, 2)
# graph.createedge(3, 2)
# graph.createedge(5, 3)
# graph.createedge(1, 4)
# print(graph.BFS(0))
# print(graph.DFS(2))
