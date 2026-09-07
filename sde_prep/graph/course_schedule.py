from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)] 
        in_degree = [0] * numCourses # Initialize in-degree array to keep track of the number of prerequisites for each course
        ans = [] # Initialize an empty list to store the order of courses that can be taken
        
        for course, prereq in prerequisites: # Build the adjacency list and in-degree array
            adj[prereq].append(course) # Add the course to the list of courses that depend on the prerequisite
            in_degree[course] += 1 # Increment the in-degree of the course
            
        q = deque() # Initialize a queue to perform BFS
        for i in range(numCourses): # Add all courses with no prerequisites to the queue
            if in_degree[i] == 0:
                q.append(i)
        
        while q: # Process the courses in the queue
            cur = q.popleft() # Get the next course from the queue
            ans.append(cur) # Add the course to the answer list
            
            for neighbor in adj[cur]: 
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0: # If the neighbor course has no more prerequisites, add it to the queue
                    q.append(neighbor)
                    
        return len(ans) == numCourses # If the number of courses in the answer list is equal to the total number of courses, return True, otherwise return False
    
# Example usage:
sol = Solution()

sol.canFinish(2, [[1, 0]]) # Output: True

        