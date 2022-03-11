class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        for num in str(n):
            product *= int(num)
        return product - sum(map(int, list(str(n))))