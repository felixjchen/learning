# grid = [[0,1,0], 
#         [1,0,1],
#         [0,1,0]]

# grid = [[1,1,0], 
#         [1,0,1], 
#         [0,1,0]]

# grid = [[1,1,0], 
#         [1,0,0],
#         [0,1,0]]

# grid = [[1,1,0],
#         [1,0,0],
#         [0,0,1]]


grid = [[1,1,0, 1, 0,1,1,0,1,1],
        [0,1,0, 0, 1,1,1,0,1,0],
        [1,0,0, 0, 0,1,0,0,0,1],
        [1,0,0, 0, 1,0,1,0,1,0],
        [1,0,0, 0, 0,1,0,0,0,1],
        [1,1,0, 0, 1,1,1,0,1,1]]

def numIsland(grid):
    rows, cols = len(grid), len(grid[0])
    num = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if i == j == 0:
                num[i][j] = grid[i][j]

            elif i == 0 and j > 0:
                if grid[i][j] == 1 and grid[i][j-1] == 0:
                    num[i][j] = num[i][j-1] + 1
                else: 
                    num[i][j] = num[i][j-1]


            elif i == 0 and j > 0:
                if grid[i][j] == 1 and grid[i][j-1] == 0:
                    num[i][j] = num[i][j-1] + 1
                else: 
                    num[i][j] = num[i][j-1]

            
            elif j== 0 and i > 0:
                if grid[i][j] == 1 and grid[i-1][j] == 0:
                    num[i][j] = num[i-1][j] + 1
                else: 
                    num[i][j] = num[i-1][j]

            else:
                if grid[i][j] == 1:
                    if grid[i-1][j] == grid[i][j-1] == 0:
                        num[i][j] = max(num[i-1][j-1], num[i-1][j], num[i][j-1]) + 1
                    else:
                        num[i][j] = max(num[i-1][j-1], num[i-1][j], num[i][j-1])
                elif grid[i][j] == 0:
                    if grid[i-1][j-1] == 0 and grid[i-1][j] == grid[i][j-1] == 1:
                        num[i][j] = num[i-1][j] + 1
                    elif num[i-1][j] == num[i][j-1]:
                        num[i][j] = num[i-1][j] + 1
                    else:
                        num[i][j] = max(num[i-1][j-1], num[i-1][j], num[i][j-1])


    from pprint import pprint
    pprint(grid)
    pprint(num)

numIsland(grid)