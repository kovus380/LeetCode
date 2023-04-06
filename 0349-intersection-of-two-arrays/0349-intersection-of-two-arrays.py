class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        for n in nums1:
            if n in nums2:
                intersection.append(n)
            
        return intersection
        