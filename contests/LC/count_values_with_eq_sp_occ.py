class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        rep = {}
        n = len(nums)
        
        for idx in range(n): 
            if nums[idx] not in rep: 
                rep[nums[idx]] = []
        
        for idx in range(n):
            rep[nums[idx]].append(idx) 
            
        count = 0
        
        for idx in rep.values():
            if len(idx) != 3:
                continue
            else:
                if idx[1] - idx[0] == idx[2] - idx[1]:
                    count += 1
                    
        return count
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1,8,1,5,1,5,8,5]
    result = solution.countSpecialIntegers(nums)
    print(result)  # Output: 1