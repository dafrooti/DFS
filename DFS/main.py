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

graph = Graph(5)
graph.createedge(1, 5)
graph.createedge(5, 2)
graph.createedge(3, 2)
graph.createedge(5, 3)
graph.createedge(1, 4)
# print(graph.BFS(0))
print(graph.DFS(2))