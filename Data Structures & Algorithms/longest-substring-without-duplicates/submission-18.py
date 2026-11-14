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

                r+=1
                maxs = max(maxs,len(count))
            else:
                count.remove(s[l])
                #print(s[l] + ' left')

                l+=1
            
        return maxs