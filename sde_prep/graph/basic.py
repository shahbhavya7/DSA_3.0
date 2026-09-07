from collections import deque

# graph = {
#     # 0: [1, 2],
#     # 1: [0, 3],
#     # 2: [0, 3],
#     # 3: [1, 2]
# }

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [2],
    4: [2],

}

visited = set()

# def dfs(adj):
#     visited = [False] * len(adj)
#     res = []
#     dfs_helper(adj, visited, 0, res)
#     return res

# def dfs_helper(adj, visited, s, res):
#     visited[s] = True # Mark the current node as visited
#     res.append(s) # Append the current node to the result list
#     for i in adj[s]: # Iterate through the neighbors of the current node
#         if not visited[i]: # If the neighbor has not been visited
#             dfs_helper(adj, visited, i, res) # Recursively call dfs_helper for the neighbor with increased depth

def dfs(adj):
    n = len(adj)
    visited = [False] * n
    res = []

    def dfs_helper(node):
        visited [node] = True
        res.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs_helper(neighbor)

    for node in range(n): # this loop is to handle disconnected components in the graph
        if not visited[node]: # if the node has not been visited, we call dfs_helper for that node
            dfs_helper(node)

def bfs(adj):
    n = len(adj)
    visited = [False] * n
    res = []

    def bfs_helper(start):
        q = deque([start]) # Initialize a queue with the starting node
        visited[start] = True

        while q: # While the queue is not empty
            node = q.popleft()
            res.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

    for node in range(n):
        if not visited[node]:
            bfs_helper(node)

    return res


# Example usage:
if __name__ == "__main__":
    result = dfs(graph)
    print(result)  # Output: [0, 1, 3, 2]

    result_bfs = bfs(graph)
    print(result_bfs)  # Output: [0, 1, 2, 3, 4]