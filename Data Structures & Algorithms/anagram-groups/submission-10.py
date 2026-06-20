class Solution:
    
    # plan:
    # write a separate function that will convert each string into a hashmap based anagram
    # create a dict where it has: key = string list anagram | val = list of strings that accompany that
    # iterate through the list -> call the helper function on each
    # if it matches the hashmap of others then append to the value
    # return dict.values()
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key = list of ints
        # value = list of strings that map to that list of ints after going through anagramString
        resDict = {}

        for s in strs:
            resList = self.anagramString(s)
            key = tuple(resList)

            if key not in resDict:
                resDict[key] = []

            resDict[key].append(s)

        return list(resDict.values())

    def anagramString(self, myStr: str) -> List[int]:
        res = [0] * 26

        for c in myStr:
            normVal = ord(c) - ord('a')
            res[normVal] += 1
        
        return res
