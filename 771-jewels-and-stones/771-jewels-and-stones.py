class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = [stone for stone in stones if stone in jewels]
        return  len(answer)
        