class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        len_arr = len(arr)
        for idx, num in enumerate(arr):
            answer += num * (((len_arr - idx) * (idx + 1) + 1) // 2)
        return answer
        