from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

queue = deque(['A'])
visited = []

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])