class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for nums in nums:
            product *= nums
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0