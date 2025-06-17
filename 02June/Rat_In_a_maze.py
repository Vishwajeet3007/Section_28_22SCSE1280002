def rat_maze(maze):
    n = len(maze)
    result = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    if maze[0][0] == 1:
        solve(0,0,n,maze,"",visited,result)
    return sorted(result)

def solve(x,y,n,maze,path,visited,result):
    if x == n-1 and y == n-1:
        result.append(path)
        return
    dir_str = 'DLRU'
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    for i in range(4):
        new_x,new_y = x + dx[i] , y + dy[i]
        if isSafe(new_x,new_y,n,maze,visited):
            visited[x][y] = True
            solve(new_x,new_y,n,maze,path + dir_str[i],visited,result)
            visited[x][y] = False

def isSafe(x,y,n,maze,visited):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]
# Example usage
maze = [
 [1, 0, 0, 0],
 [1, 1, 0, 1],
 [0, 1, 0, 0],
 [1, 1, 1, 1]
]

print(rat_maze(maze))  
