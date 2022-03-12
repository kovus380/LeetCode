class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = []
        while True:
            print(prev_nums)
            temp_n = str(n)
            temp_sum = 0
            for char in temp_n:
                temp_sum += (int(char)) ** 2
            if temp_sum == 1:
                return True
            if temp_sum in prev_nums:
                return False
            prev_nums.append(temp_sum)
            n = temp_sum