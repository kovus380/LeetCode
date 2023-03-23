class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for idx in range(1, len(prices)):
            if prices[idx] - prices[idx - 1] > 0:
                answer += prices[idx] - prices[idx - 1]
        return answer