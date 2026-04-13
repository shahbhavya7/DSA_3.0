class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        stri = ""
        for i in nums:
            stri  = stri + str(i)
        count = 0
        for i in stri:
            if i == str(digit):
                count = count + 1
        return count