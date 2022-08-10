class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[(end + start) // 2] == target:
                return ((end + start) // 2)
            elif nums[(end + start) // 2] < target:
                start = (end + start) // 2 + 1
            elif nums[(end + start) // 2] > target:
                end = (end + start) // 2 - 1
        return -1