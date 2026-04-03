class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create two pointers at the ends of the string
        left_ptr = 0
        right_ptr = len(s) - 1

        # Check each pair of opposing alphanumeric characters
        while left_ptr < right_ptr:
            left_char = s[left_ptr]
            right_char = s[right_ptr]

            # Set left pointer
            while not left_char.isalnum() and left_ptr < right_ptr:
                left_ptr += 1
                left_char = s[left_ptr]

            # Set right pointer
            while not right_char.isalnum() and right_ptr > left_ptr:
                right_ptr -= 1
                right_char = s[right_ptr]

            # If left and right are non-alphanumeric, we're done
            if not left_char.isalnum() and right_char.isalnum():
                return False

            # If left and right don't match, we're done
            if left_char.lower() != right_char.lower():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True
