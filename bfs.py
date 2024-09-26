from collections import deque
from collections import defaultdict


'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        while len(queue) != 0:
        tmpnode = queue.popleft()
        for node in graph[tmpnode]:
            if not visited[node]:
                path.append(node)
                queue.append(node)
                visited[node] = True
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = input().split()
    graph[u].append(v)
    graph[v].append(u)

start = ''
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
