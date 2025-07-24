"""Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
Output: [-1,-2,-2]
Explanation: There are 3 subarrays with size k = 3. 
The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1. 
The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2. 
The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2."""
class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        n = len(nums)
        freq = [0] * 51      # freq[j] = count of -j in the current window
        result = []

        # 1) Build initial window
        for i in range(k):
            val = nums[i]
            if val < 0:
                freq[-val] += 1

        # 2) Helper to find the x-th smallest negative
        def find_beauty():
            running = 0
            for j in range(50, 0, -1):  # j=50 → -50, ... j=1 → -1
                running += freq[j]
                if running >= x:
                    return -j
            return 0

        # 3) Record beauty of the first window
        result.append(find_beauty())

        # 4) Slide the window through the rest of the array
        for i in range(k, n):
            old = nums[i - k]
            if old < 0:
                freq[-old] -= 1

            new = nums[i]
            if new < 0:
                freq[-new] += 1

            result.append(find_beauty())

        return result

# Example usage:
print(Solution().getSubarrayBeauty([1, -1, -3, -2, 3], k=3, x=2))
# Output: [-1, -2, -2]

        