from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num) # Push the current number onto the min-heap

            if len(min_heap) > k: # If the size of the min-heap exceeds k, pop the smallest element from the heap as we are only interested in the k largest elements
                heapq.heappop(min_heap)

        return min_heap[0]  # The root of the min-heap is the kth largest element



# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = solution.findKthLargest(nums, k)
    print(result)  # Output: 5