"""
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

Insert when a larger number is encountered, then remove the last element to maintain size.
"""

from typing import List

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		length = m + n
		for i in range(n):
			num2 = nums2[i]
			for j in range(length):
				num1 = nums1[j]
				if (num1 > num2 or (j >= m + i and num1 == 0)):
					nums1.insert(j, num2)
					nums1.pop(length)
					break
