class Solution:

    """
    plan:
    - iterate through the whole list
    - create a dict -> key = value, val = freq
    - create a list of lists of size len(nums) +1

    - walk thorugh dict.items(), append each list[freq val] with the index
    - then walk backwards on the list until you populated enough
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqCounter = {} # key = value | val = freq

        for i, num in enumerate(nums):
            freqCounter[num] = freqCounter.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]

        for key, val in freqCounter.items():
            bucket[val].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if (len(res) == k):
                    return res
        
        return res