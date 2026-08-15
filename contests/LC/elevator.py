class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        
        tt = 0
        
        tt = abs(0 - requests[0])
        
        for i in range(n - 1):
            tt += abs(requests[i] - requests[i + 1])
            
        return tt