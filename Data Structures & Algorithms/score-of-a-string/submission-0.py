class Solution:
    def scoreOfString(self, s: str) -> int:
        stringScore = 0
        for i in range(len(s) - 1):
            stringScore += abs(ord(s[i]) - ord(s[i+1]))
        return stringScore
