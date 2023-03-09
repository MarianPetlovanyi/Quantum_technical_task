from collections import deque
def check_coords(i, max_i):
    if 0<=i<max_i:
        return True
    return False

def calculate_islands(matrix) -> int:
    islands = 0
    rows = len(matrix)
    columns = len(matrix[0])
    visited = [[False]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if not visited[i][j] and matrix[i][j] == 1:
                islands+=1
                queue = deque()
                queue.append([i,j])
                while len(queue) != 0:
                    front_i, front_j = queue.pop()
                    visited[front_i][front_j]=True
                    if check_coords(front_j-1, columns) and visited[front_i][front_j-1] and matrix[front_i][front_j-1] == 1:
                        queue.append([front_i,front_j-1])
                    if check_coords(front_j+1, columns) and not visited[front_i][front_j+1] and matrix[front_i][front_j+1] == 1:
                        queue.append([front_i,front_j+1])
                    if check_coords(front_i+1, rows) and not visited[front_i+1][front_j] and matrix[front_i+1][front_j] == 1:
                        queue.append([front_i+1,front_j])
    return islands

if __name__ == '__main__':
    matrix_list = [
            [
                [0,1,0],
                [0,0,0],
                [0,1,1]
            ],#2
            [
                [0,0,0,1],
                [0,0,1,0],
                [0,1,0,0]
            ],#3
            [
                [1,1,0,1],
                [0,1,0,0],
                [0,1,0,0],
                [0,0,1,1]
            ],#3
            [
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ],#1
            [
                [0,0],
                [0,0],
                [0,0]
            ],#0
            [
                [1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 0, 0, 0, 1],
                [0, 1, 0, 0, 1]
            ]#7

        ]
    for matrix in matrix_list:
        print(calculate_islands(matrix))
