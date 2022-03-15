class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        for i in range(len(s)):
            temp = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in temp:
                    break
                temp += s[j]
            subs.append(len(temp))
        return max(subs) if subs else 0
        