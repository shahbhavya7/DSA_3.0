from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)  # Initialize the answer list with zeros
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        return ans


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = solution.dailyTemperatures(temperatures)
    print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]