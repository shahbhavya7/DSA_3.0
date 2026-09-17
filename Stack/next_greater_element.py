from typing import List

class Solution:
    def nextGreaterElementbrute(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums1)):
            i = nums2.index(nums1[x]) # find the index of the current element of nums1 in nums2
            greater = -1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums1[x]:
                    greater = nums2[j]
                    break
            ans.append(greater)
        return ans
                   
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # stack to keep track of the elements for which we haven't found the next greater element yet
        ng = {} # dictionary to store the next greater element for each element in nums2
        
        for x in nums2: # iterate through each element in nums2
            while stack and stack[-1] < x: # while the stack is not empty and the top element of the stack is less than the current element x
                ng[stack.pop()] = x # the next greater element for the popped element is x
            stack.append(x) # at the end of loop we  get
            
        for x in stack:
            ng[x] = -1
        ans = []
        for x in nums1:
            ans.append(ng[x])
        return ans
        
