from collections import deque, defaultdict
import heapq

def bfs(grid, visited, start, island_id):
    """Flood-fill to mark islands with unique IDs."""
    n, m = len(grid), len(grid[0])
    queue = deque([start])
    visited[start[0]][start[1]] = True
    grid[start[0]][start[1]] = island_id

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                grid[nx][ny] = island_id
                queue.append((nx, ny))

def find_bridges(grid, island_count):
    """Find all valid bridges between islands and their lengths."""
    n, m = len(grid), len(grid[0])
    bridges = []
    
    # Directions: vertical and horizontal
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(n):
        for y in range(m):
            if grid[x][y] > 0:  # Part of an island
                island_id = grid[x][y]
                for dx, dy in directions:
                    length = 0
                    nx, ny = x + dx, y + dy

                    while 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == island_id:
                            break  # Same island
                        if grid[nx][ny] > 0:
                            if length >= 2:
                                bridges.append((length, island_id, grid[nx][ny]))
                            break

                        nx += dx
                        ny += dy
                        length += 1

    return bridges

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def minimum_bridge_length(grid):
    n, m = len(grid), len(grid[0])

    # Step 1: Identify islands
    visited = [[False] * m for _ in range(n)]
    island_id = 2  # Start from 2 to distinguish from 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(grid, visited, (i, j), island_id)
                island_id += 1

    island_count = island_id - 2

    # Step 2: Find all possible bridges
    bridges = find_bridges(grid, island_count)

    # Step 3: Minimum Spanning Tree (Kruskal's algorithm)
    parent = {i: i for i in range(2, island_id)}
    rank = {i: 0 for i in range(2, island_id)}

    bridges.sort()  # Sort by length
    total_length = 0
    edges_used = 0

    for length, island_a, island_b in bridges:
        if find(parent, island_a) != find(parent, island_b):
            union(parent, rank, island_a, island_b)
            total_length += length
            edges_used += 1

    # Check if all islands are connected
    if edges_used == island_count - 1:
        return total_length
    else:
        return -1

# Input
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output
print(minimum_bridge_length(grid))
