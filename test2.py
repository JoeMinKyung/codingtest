from collections import deque

def numIslands(grid):
    num_of_islands=0
    row=len(grid)
    col=len(grid[0])
    visited=[[False]*col for _ in range(row)]
   
    
    def bfs(x,y):
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        visited[x][y]=True
        q=deque()
        q.append((x,y))
        
        while q:
            cur_x,cur_y=q.popleft()
            
            for i in range(4):
                next_x=cur_x+dx[i]
                next_y=cur_y+dy[i]
                
                if 0<=next_x<row and 0<=next_y<col:
                   
                    if visited[next_x][next_y]==False and grid[next_x][next_y]=="1":
                        q.append((next_x,next_y))
                        visited[next_x][next_y]=True
        return visited
    
    for i in range(row):
        
        for j in range(col):
            
            if grid[i][j]=="1" and not visited[i][j]:
                bfs(i,j)
                num_of_islands+=1
    
    return num_of_islands
grid1=[
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
]
grid2=[
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1'],
]

print(numIslands(grid1))
print(numIslands(grid2))
