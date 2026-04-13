from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # if total gas is less than total cost, it's impossible to complete the circuit
            return -1
        start = 0
        current_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i] # add the net gas (gas - cost) at each station
            if current_gas < 0: # if current gas is negative, we cannot start from the previous station, so we reset the start and current_gas
                start = i + 1
                current_gas = 0
        return start

# Example usage:
solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
