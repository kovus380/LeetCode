class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        different_char = []
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                different_char.append([ch1, ch2])
        if not different_char:
            return True
        if len(different_char) != 2:
            return False
        if different_char[0][0] == different_char[1][1] and different_char[0][1] == different_char[1][0]:
            return True
        else:
            return False
                                     