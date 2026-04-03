from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        start = 0
        end = 0
        for i in range(len(s)):
            for j in range(len(words)):
                char = s[i]
                word  = words[j]
                if char == word[start % i]:
                    # match
                    pass
                
        return indices
        
s = "barfoothefoobarman"
words = ["foo","bar"]
solution = Solution()
print(solution.findSubstring(s, words))
