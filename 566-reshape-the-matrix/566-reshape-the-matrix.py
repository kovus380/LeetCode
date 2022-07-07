class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nums, answer = [], []
        for row in mat:
            nums += row
        if len(nums) != r * c:
            return mat
        else:
            return [nums[i : i + c] for i in range(0, len(nums), c)]
        