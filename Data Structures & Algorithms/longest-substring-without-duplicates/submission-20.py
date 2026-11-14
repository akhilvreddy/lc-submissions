class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()

        l = 0 
        r = 0
        maxs = 0

        while l < len(s) and r<len(s):
            if s[r] not in count:
                count.add(s[r])
                #print(s[r] + ' right')
                maxs = max(maxs,r-l+1)

                r+=1
            else:
                count.remove(s[l])
                #print(s[l] + ' left')

                l+=1
            
        return maxs