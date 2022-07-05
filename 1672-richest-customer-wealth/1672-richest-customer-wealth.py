class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most_wealth = 0
        for account in accounts:
            most_wealth = max(most_wealth, sum(account))
        return most_wealth
        