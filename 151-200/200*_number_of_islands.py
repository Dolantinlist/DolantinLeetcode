class Solution:
    def numbIslands(self, grid):
        if not grid:
            return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    queue = []
                    queue.append([i, j])
                    while queue:
                        x, y = queue.pop(0)
                        if x > 0 and grid[x - 1][y] == '1':
                            grid[x - 1][y] = '#'
                            queue.append([x - 1, y])
                        if y > 0 and grid[x][y - 1] == '1':
                            grid[x][y - 1] = '#'
                            queue.append([x, y - 1])
                        if x < len(grid) - 1 and grid[x + 1][y] == '1':
                            grid[x + 1][y] = '#'
                            queue.append([x + 1, y])
                        if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
                            grid[x][y + 1] = '#'
                            queue.append([x, y + 1])
                    cnt += 1
        return cnt
