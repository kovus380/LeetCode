class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        no_zero = 0
        for idx, num in enumerate(nums):
            if num:
                nums.pop(idx)
                nums.insert(no_zero, num)
                no_zero += 1
                