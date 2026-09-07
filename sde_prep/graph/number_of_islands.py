from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or  j >= len(grid[0]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'  # no need to keep track of visited nodes, we can just mark them as '0' in the grid itself
        self.dfs(grid, i + 1, j)  # down
        self.dfs(grid, i - 1, j)  # up
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)  # left


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = solution.numIslands(grid)
    print(result)  # Output: 3
    