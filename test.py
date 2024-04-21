from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    visited=[[False]*col for _ in range(row)]
    
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(8):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
grid=[
    [0,0,0,1,0,0,0],
    [0,1,1,1,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,0,1,1,1,0],
    [0,1,0,0,0,0,0]
]