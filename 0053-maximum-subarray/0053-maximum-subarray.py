class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums[1:]:
            dp.append(max(dp[-1] + num, num))

        return(max(dp))