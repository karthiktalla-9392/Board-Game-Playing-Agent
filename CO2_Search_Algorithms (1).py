from collections import deque

graph = {'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}

def bfs(start):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dfs(start, visited=None):
    if visited is None:
        visited=[]
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node, visited)
    return visited

print("BFS:", bfs('A'))
print("DFS:", dfs('A'))
