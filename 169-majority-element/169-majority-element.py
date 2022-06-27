from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return list(Counter(nums).most_common())[0][0]