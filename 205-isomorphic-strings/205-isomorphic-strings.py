from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        answer = ""
        ch = []
        match = defaultdict()
        for idx, c in enumerate(s):
            if c not in match:
                if t[idx] in ch:
                    return False
                ch.append(t[idx])
                match[c] = t[idx]
            answer += match[c]
        print(answer, t)
        return True if answer == t else False