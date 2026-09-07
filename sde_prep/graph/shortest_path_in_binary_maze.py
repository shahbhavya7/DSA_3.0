from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n -1] != 0:
            return -1 # if the starting or ending point is blocked, return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] # down, up, right, left, and the four diagonals
        q = deque([(0, 0, 1)]) # queue with the starting point (0, 0) and the initial distance of 1 

        grid[0][0] = 1 # mark the starting point as visited

        while q:
            i, j, dist = q.popleft() # get the current position and distance

            if i == n - 1 and j == n - 1: # if we have reached the bottom-right corner
                return dist

            for di,dj in directions:
                ni, nj = i + di, j + dj # calculate the new position

                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0: # if the new position is within bounds and not visited
                    grid[ni][nj] = 1 # mark the new position as visited
                    q.append((ni, nj, dist + 1))

        return -1 # if we have exhausted all possibilities and haven't reached the bottom-right corner


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [0, 0, 0 ],
        [1, 1, 0 ],
        [1, 1, 0 ]
    ]
    result = solution.shortestPathBinaryMatrix(grid)
    print(result)  # Output: 4