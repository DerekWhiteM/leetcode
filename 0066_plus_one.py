"""
https://leetcode.com/problems/plus-one/description/

Get the numerical value, increment, then create a new array.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = self.getValue(digits)
        value += 1
        return self.toArray(value)
    
    def getValue(self, digits: List[int]) -> int:
        value = 0
        for i in range(len(digits)):
            digit = digits[len(digits) - 1 - i]
            multiplier = 10 ** i
            value += (digit * multiplier)
        return value

    def toArray(self, value: int) -> List[int]:
        arr = []
        num = value
        while num > 0:
            digit = num % 10
            print(digit)
            arr.insert(0, digit)
            num //= 10
        return arr
