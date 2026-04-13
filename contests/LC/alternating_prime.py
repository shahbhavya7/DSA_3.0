class Solution:
    
    def sieve_array(self, n: int) -> list[bool]:
        prime_nos = [True for i in range(n + 1)]
        prime_nos[0] = prime_nos[1] = False
        pre = 2
        while (pre * pre <= n):
            if (prime_nos[pre] == True):
                for i in range(pre * pre, n + 1, pre):
                    prime_nos[i] = False 
            pre += 1
        return prime_nos
    
    def minOperations(self, nums: list[int]) -> int:
        sieve_array = self.sieve_array(2*max(nums))
        op_cnt = 0
        for i in range(len(nums) - 1):
            if (i%2 != 0):
                if (sieve_array[nums[i]] == True):
                    if (sieve_array[nums[i]] and sieve_array[nums[i + 1]]): 
                        op_cnt = op_cnt + 2
                    else:
                        op_cnt = op_cnt + 1
            else: 
                if (sieve_array[nums[i]] == False): 
                    while not sieve_array[nums[i]]: 
                        nums[i] = nums[i] + 1
                        op_cnt = op_cnt + 1
        return op_cnt