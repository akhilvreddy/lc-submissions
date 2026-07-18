class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def expand(l, r):
            nonlocal res
            if l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    expand(l-1, r + 1)


        # odd length
        for i in range(len(s)):
            expand(i, i)

        # even length
        for i in range(len(s) - 1):
            expand(i, i+1)
        
        return res