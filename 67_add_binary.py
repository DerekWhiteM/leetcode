"""
https://leetcode.com/problems/add-binary/description/

Use binary addition.
"""

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		length_a = len(a)
		length_b = len(b)
		
		result = []
		carry = 0

		for i in range(max(length_a, length_b)):
			int_a = int(a[length_a - 1 - i]) if (i < length_a) else 0
			int_b = int(b[length_b - 1 - i]) if (i < length_b) else 0
			sum = int_a + int_b + carry
			carry = sum // 2
			result.append(sum % 2)

		if carry:
			result.append(1)

		return ''.join(map(str, result[::-1])) 

solution = Solution()
print(solution.addBinary('1010', '1011'))