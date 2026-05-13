class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]

        num_centers = 2 * len(s) - 1
        best_left = 0
        best_right = 1

        # for each center, expand while chars on each side match
        # start between first and second char

        for i in range(num_centers):
            left = 0
            right = 0

            if i % 2 == 0:
                # when i is even, you are between two chars
                left = i // 2
                right = left + 1
            else:
                # when i is odd, you are on a char
                char = i // 2 + 1
                left = char - 1
                right = char + 1

            current_best_left = 0
            current_best_right = 0

            # expand out from the center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_best_left = left
                current_best_right = right
                left -= 1
                right += 1

            # compare current to longest palindrome
            if current_best_right - current_best_left > best_right - best_left:
                best_left = current_best_left
                best_right = current_best_right

        return s[best_left : best_right + 1]
