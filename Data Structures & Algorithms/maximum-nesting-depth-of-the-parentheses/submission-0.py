class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        curr = 0
        for c in s:
            if c == '(':
                curr += 1
            if c == ')':
                curr -= 1
            m = max(m, curr)
        
        return m


        