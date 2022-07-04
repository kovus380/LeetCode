class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        for i in range(1, len(arr) + 1, 2):
            for start in range(len(arr) - i + 1):
                answer += sum(arr[start : start+i])
        return answer
        