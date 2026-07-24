class Solution:
    def validPalindrome(self, s: str) -> bool:
        used = False

        def parse(l, r, used):
            if l <= r:
                if s[l] != s[r]:
                    if used:
                        return False
                    return parse(l+1, r, True) or parse(l, r-1, True)
                return parse(l+1, r-1, used)
            return True
        
        return parse(0, len(s)-1, False)
        