from collections import deque

grid = [
    ['S', '.', '.'],
    ['#', '#', '.'],
    ['.', '.', 'G']
]

queue = deque([(0, 0)])
visited = set()
visited.add((0, 0))

moves = [(0,1), (1,0), (0,-1), (-1,0)]

while queue:

    x, y = queue.popleft()

    print("Robot at:", (x, y))

    if grid[x][y] == 'G':
        print("Goal reached!")
        break

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if (0 <= nx < 3 and 0 <= ny < 3
            and grid[nx][ny] != '#'
            and (nx, ny) not in visited):

            visited.add((nx, ny))
            queue.append((nx, ny))
