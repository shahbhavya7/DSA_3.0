from typing import List

class Solution:

    def dfs(self, node: int, adj_list: List[List[int]], visited: List[bool]) -> None:
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj_list = [[] for _ in range(V)]  # create an adjacency list for the graph

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False] * V

        cnt = 0

        for i in range(V):
            if not visited[i]:
                cnt += 1 # if not visited, we found a new province, so we increment the count
                self.dfs(i, adj_list, visited)

        return cnt


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    result = solution.findCircleNum(isConnected)
    print(result)  # Output: 2