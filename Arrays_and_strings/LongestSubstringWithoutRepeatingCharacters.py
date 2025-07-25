''''Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()    
        left = 0           
        result = 0         
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            
            charSet.add(s[right])

            
            current_length = right - left + 1
            result = max(result, current_length)

        return result


s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))  
