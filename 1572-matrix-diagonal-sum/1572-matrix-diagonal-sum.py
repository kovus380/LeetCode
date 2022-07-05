class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        for idx, m in enumerate(mat):
            m_set = set([idx, len(m) - idx - 1])
            answer += sum([mat[idx][num] for num in m_set])
        return answer