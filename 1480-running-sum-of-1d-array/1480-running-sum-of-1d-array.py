class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 0
        for num in nums:
            answer.append(temp + num)
            temp = answer[-1]
        return answer