class Solution:

    """
    plan:
    - initialize a dict || key = current val, val = current index
    - enumerate through nums
    - check if target - current value exists in the keys of dict
    - if yes, return dict[(target-currVal)], i
    - if no, add value to dict
    - return [] as default case (should never hit that according to problem) 
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # key = current value | val = current index

        for index, num in enumerate(nums):
            difference = target - num

            if difference in seen: 
                return [seen[difference], index]

            else:
                seen[num] = index
        
        return []