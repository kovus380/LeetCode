class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        correct = 0
        for i in range(len(t)):
            if correct == len(s):
                return True
            if t[i] == s[correct]:
                correct += 1
        if correct == len(s):
            return True
        print(correct)
        return False
        