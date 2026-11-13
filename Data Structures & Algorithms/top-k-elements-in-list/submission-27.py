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

        maps = {}

        for i in nums:
            maps[i] = maps.get(i, 0) + 1

        arr = [[] for x in range(len(nums)+1)]


        for num, freq in maps.items():
            arr[freq].append(num)

        count = len(arr)
        result = []

        for freq in range(len(arr)-1, 0, -1):
            for num in arr[freq]:
                result.append(num)
                if len(result)==k: return result
                if count == 0: return result


        