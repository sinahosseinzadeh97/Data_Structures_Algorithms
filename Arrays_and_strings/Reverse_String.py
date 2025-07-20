'''Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory
Example:Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right=len(s)-1
        left = 0
        while left <right:
            temp = s [left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

s = ["h","e","l","l","o"]
print(Solution().reverseString(s))