class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            if target - nums[i] in nums[i + 1:]:
                print(target - nums[i])
                print(nums[i:].index(target - nums[i]))
                return [i, (i + 1) + nums[i + 1:].index(target - nums[i])]
        