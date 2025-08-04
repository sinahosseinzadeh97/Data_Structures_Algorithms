'''Minimum Value to Get Positive Step by Step Sum
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2'''
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize cumulative sum and minimum prefix sum
        current_sum = 0
        min_pref = 0

        # compute prefix sums and track the minimum
        for num in nums:
            current_sum += num
            min_pref = min(min_pref, current_sum)

        # determine the smallest positive start value
        # 1 - min_pref shifts the lowest prefix sum to exactly 1
        # if this value is less than 1, we default to 1
        required_start = 1 - min_pref
        return required_start if required_start > 1 else 1

