class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create a list of length 26 and keep adding to it based on ascii index
        # compare at the end 

        if len(s) != len(t): 
            return False
        
        sList, tList = [0]*26, [0]*26

        for c in s:
            asciiVal = ord(c) - ord('a')
            sList[asciiVal] += 1

        for c in t:
            asciiVal = ord(c) - ord('a')
            tList[asciiVal] += 1

        return sList == tList