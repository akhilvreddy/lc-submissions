from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        
        return all(v == 0 for v in counts.values())
        
        