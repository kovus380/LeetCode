class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()
        for idx, num in enumerate(nums):
            if num == 0:
                return 0
            if num > 0:
                if idx % 2 == 0:
                    return 1
                else:
                    return -1
        return -1