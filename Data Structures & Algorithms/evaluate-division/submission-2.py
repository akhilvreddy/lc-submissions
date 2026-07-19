from collections import defaultdict
class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for eq, val in zip(equations, values):
            var1, var2 = eq
            graph[var1][var2] = val
            graph[var2][var1] = 1/val
        
        nodes = set(graph.keys())
        def findPath(v1, v2, ans, visited):
            if v1 in nodes and v1 == v2:
                return ans
        
            for neighbor, length in graph[v1].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    boom = findPath(neighbor, v2, ans*length, visited)
                    if boom != -1:
                        return boom
                    
            
            return -1


        
        res = []
        for v1, v2 in queries:
            curProd = 1

            res.append(findPath(v1, v2, 1, {v1}))
        
        return res
            


    






        