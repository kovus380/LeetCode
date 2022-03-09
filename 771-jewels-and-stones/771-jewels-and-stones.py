class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        print(jewel)
        
        answer = [stone for stone in stones if stone in jewel]
        return len(answer)
            
        