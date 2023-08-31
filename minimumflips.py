#1318. Minimum Flips to Make a OR b Equal to c

class Solution:
    def minFlips(self, a, b, c):
        ab, equal, ans = a | b, (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if equal & mask > 0:
                if (a & mask) == (b & mask) and (c & mask) == 0:
                    ans += 2 
                else:
                    ans += 1
        return ans
