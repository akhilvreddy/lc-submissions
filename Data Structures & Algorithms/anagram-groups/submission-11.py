from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lists = defaultdict(list)

        for s in strs:
            
            arr = [0]*26

            for char in s:
                arr[ord(char) - ord('a')]+=1
            
            lists[tuple(arr)].append(s)
        return list(lists.values())