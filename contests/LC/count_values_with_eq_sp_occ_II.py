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
            if len(idx) < 3:
                continue
            else:
                flag = True
                for i in range(1, len(idx) - 1):
                    if idx[i] - idx[i - 1] != idx[i + 1] - idx[i]:
                        flag = False
                        break
                if flag:
                    count += 1
                    
        return count
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [8,8,8,8]
    result = solution.countSpecialIntegers(nums)
    print(result)  # Output: 1