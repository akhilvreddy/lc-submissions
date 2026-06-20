class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen, pair = len(s), (0, 0)
        resolved = 0

        tDict = defaultdict(int)
        for c in t:
            tDict[c] += 1
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tDict:
                tDict[c] -= 1
                if tDict[c] == 0:
                    resolved += 1

            while resolved == len(tDict):
                if (r-l+1) <= minLen:
                    minLen = r-l+1
                    pair = (l, r+1)
                if s[l] in tDict:
                    tDict[s[l]] += 1
                    if tDict[s[l]] > 0:
                        resolved -= 1
                l += 1
        

        return s[pair[0]:pair[1]]

        
        


        