from collections import defaultdict
from pprint import pprint

serversNum = 4
connectionsNum = 4
connections = [[1, 2], [1, 3], [3, 2], [3, 4]]

class Solution:
    def criticalConnections(self, n, connections):

        graph = defaultdict(list)
        # Adj list rep of graph
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        disc = [None for _ in range(n+1)]
        low = [None for _ in range(n+1)]


        self.c = 0 

        def dfs(root, pred):
            if disc[root] is None:
                disc[root] = self.c
                low[root] = self.c

                self.c += 1

                for child in graph[root]:
                    if disc[child] is None:
                        dfs(child, root)
                
                if pred is not None:
                    l = min([low[child] for child in graph[root] if child != pred] + [low[root]])
                else:
                    l = min([low[child] for child in graph[root]] + [low[root]])

                low[root] = l
        dfs(1, None)

        pprint(low)
        pprint(disc)

        # pprint(graph)

print(Solution().criticalConnections(serversNum, connections))