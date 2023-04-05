class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        s.sort()
        answer = 0
        greed = 0
        
        for size in s:
            if greed >= len(g):
                break
            if size >= g[greed]:
                answer += 1
                greed += 1
        return answer
        