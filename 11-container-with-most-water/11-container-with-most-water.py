class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        answers = []
        while start >= 0 and end < len(height) and start < end:
            answers.append((end - start) * min(height[end], height[start]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max(answers)