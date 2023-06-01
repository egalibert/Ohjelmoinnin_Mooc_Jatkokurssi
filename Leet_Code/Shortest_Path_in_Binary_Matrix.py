from collections import deque

class Solution:
    def shortestPathBinaryMatrix(grid: list) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        x = len(grid)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([(0, 0)])
        visited = [[False] * n for x in range(n)]
        distances = [['not used'] * n for x in range(n)]
        distances[0][0] = 1
        visited[0][0] = True

        while queue:
            row, col = queue.popleft()
            if row == n - 1 and col == n - 1:
                return distances[row][col]
            for dir_row, dir_col in directions:
                next_row = row + dir_row
                next_col = col + dir_col
                if 0 <= next_row < n and 0 <= next_col < n and visited[next_row][next_col] == False and grid[next_row][next_col] == 0:
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    distances[next_row][next_col] = distances[row][col] + 1
        return (-1)

def main():
    grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
    result = Solution.shortestPathBinaryMatrix(grid)
    print(result)

main()
