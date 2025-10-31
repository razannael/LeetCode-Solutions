class Solution:
	def findLHS(self, nums: List[int]) -> int:
		tmp = Counter(nums)
		keys = tmp.keys()
		max = 0
		for num in keys:
			if num - 1 in keys:
				if tmp[num - 1] + tmp[num] > max:
					max = tmp[num - 1] + tmp[num]
		return max