from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        total = 0 # total number of oranges (fresh + rotten)
        count = 0 # count of fresh oranges that have rotted during the BFS process

        # Step 1: Add all rotten oranges to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: # if the orange is rotten put it in the queue
                    queue.append((r, c))

                if grid[r][c] != 0: # count all oranges (fresh + rotten)
                    total += 1 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
        minutes = 0


        # Step 2: BFS to rot the fresh oranges
        while queue:
            k = len(queue) # number of rotten oranges at the current minute is equal to the size of the queue
            count += k # increment the count of rotted oranges by the number of rotten oranges at the current minute
            for _ in range(k):
                r,c = queue.popleft() # get the coordinates of the rotten orange
                for dr, dc in directions: # check all 4 directions
                    nr, nc = r + dr, c + dc # new coordinates of the adjacent cell
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # rot the fresh orange
                        queue.append((nr, nc))

            if queue: # if there are still rotten oranges in the queue, increment the minutes counter
                minutes += 1

        # Step 3: Check if all oranges have rotted
        return minutes if count == total else -1


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    result = solution.orangesRotting(grid)
    print(result)  # Output: 4

