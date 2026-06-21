class Solution:
    
    """
    plan:
    create a new dict -> key = unique number | val = frequency of the number
    sort list
    iterate through nums and populate dict
    create a new list of length len(nums) + 1, where each element is its own empty list for now
    iterate through the dict.items() and append each key into the val index in the list
    walk through the resulting list in reverse and append each value of the list into the list. once you hit K then retrun the list
    """
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {} # key = number || val = frequency
        freqList = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        for num, freq in freqDict.items():
            freqList[freq].append(num)
        
        res = []

        for i in range(len(freqList)-1, 0, -1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []
