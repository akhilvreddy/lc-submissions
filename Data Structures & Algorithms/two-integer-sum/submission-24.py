class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        indicies = {}

        for i,n in enumerate(nums):
            if n in indicies:
                return [indicies[n], i]
            indicies[target - n] = i
        return []

        