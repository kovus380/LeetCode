class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num in nums1:
            answer.append(-1)
            for num_2 in nums2[nums2.index(num):]:
                if num_2 > num:
                    answer[-1] = max(-1, num_2)
                    break
        return answer