from collections import deque
matrix = [[1, 1, 0, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 1],
          [0, 1, 1, 1]]
def Maze(matrix):
    q = deque()
    m = len(matrix[0])
    n = len(matrix)
    q.append((0, 0))
    count = 0
    while (len(q) > 0):
        p = q.popleft()
        if (p[0] == n - 1 and p[1] == m - 1):
            count += 1
        if (p[0] + 1 < n and matrix[p[0] + 1][p[1]] == 1):
          q.append((p[0] + 1, p[1]))
        if (p[1] + 1 < m and matrix[p[0]][p[1] + 1] == 1):
          q.append((p[0], p[1] + 1))
    return count
print(Maze(matrix))
def dfs(matrix, visited, path, x, y):
    visited[x][y] = True
    path.append((x, y))
    m = len(matrix[0])
    n = len(matrix)
    if x == n - 1 and y == m - 1:
        return True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] == 1:
            if dfs(matrix, visited, path, nx, ny):
                return True
    path.pop()
    visited[x][y] = False
    return False

def Mazedfs(matrix):
    m = len(matrix[0])
    n = len(matrix)
    visited = [[False for i in range(m)] for j in range(n)]
    path = []
    dfs(matrix, visited, path, 0, 0)
    return path

path = Mazedfs(matrix)
print(path)
