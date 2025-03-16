"""
https://leetcode.com/problems/length-of-last-word/description/

Start from the end of the string and count up until a space is found.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        count = 0
        for i in range(end, -1, -1):
            if s[i] == ' ':
                if count:
                    return count
            else:
                count += 1
        return count 
