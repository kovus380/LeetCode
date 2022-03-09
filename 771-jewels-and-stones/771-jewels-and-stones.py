class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = collections.defaultdict(int)
        for j in  jewels:
            jewel[j] = 1
        
        answer = [stone for stone in stones if stone in jewel]
        return len(answer)
            
        