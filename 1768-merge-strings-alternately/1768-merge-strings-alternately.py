class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        w1, w2, end = 0, 0, len(word1) + len(word2)
        for i in range(end):
            if w1 < len(word1):
                answer += word1[w1]
                w1 += 1
            if w2 < len(word2):
                answer += word2[w2]
                w2 += 1
        return answer