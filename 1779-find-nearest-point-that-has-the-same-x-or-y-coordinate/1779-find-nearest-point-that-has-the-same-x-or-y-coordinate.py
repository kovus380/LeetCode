class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = []
        for idx, point in enumerate(points):
            if x == point[0] or y == point[1]:
                answer.append([abs(x - point[0]) + abs(y - point[1]), idx])
        answer.sort()
        return answer[0][1] if answer else -1