class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, value in enumerate(nums):
            if value >= target:
                return idx
        return len(nums)
        