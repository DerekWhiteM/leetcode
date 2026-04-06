class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            dict_s[char_s] = dict_s.get(char_s, 0) + 1
            dict_t[char_t] = dict_t.get(char_t, 0) + 1
        return dict_s == dict_t
        
solution = Solution()

print(solution.isAnagram("rat", "car"))
