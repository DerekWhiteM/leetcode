from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        current_match = 0
        indices = []
        start = 0
        end = 1 
        
        for i in range(len(s)):
            for j in range(len(words)):
                sliding_window = s[start:end] # 1,2: ba
                word  = words[j] # bar
               
               # Case 1: sliding_window matches the word or a substring of it 
                if sliding_window == word[start:end]:
                    end += 1
                    continue
                    
                # Case 2: sliding_window is longer, and must be compared with permutations
                
                else 
                
        return indices
        
s = "barfoothefoobarman"
words = ["foo","bar"]
solution = Solution()
print(solution.findSubstring(s, words))
