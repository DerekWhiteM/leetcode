"""
https://leetcode.com/problems/majority-element/description

Use the Boyer-Moore majority vote algorithm.
"""

from typing import List

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		m = c = 0 
		for x in nums:
			if c == 0:
				m = x
				c = 1
			elif m == x:
				c = c + 1
			else:
				c = c - 1
		return m 
		