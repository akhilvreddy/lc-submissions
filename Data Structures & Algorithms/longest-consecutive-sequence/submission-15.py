class Solution:

    """
    plan:

    initialize a maxLen counter (initially set to 0)
    initialize hashset that is a replica of the actual set since it gives us the ability to do O(1) lookups
    iterate through the list in a for loop
    if num - 1 exists in the list, then skip
    if num - 1 doesn't exit, then that means it is a beginning of a sequence
        - start a while loop that keeps going wihle the next increment exists in the hashset
        - increment counter for that
        - take set maxLen = max(maxLen, counter)
    
    return maxConsecutive
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        maxConsecutive = 1
        
        for num in nums:
            ptr = num
            counter = 1

            if (num - 1) not in numSet:
                continue

            if (num - 1) in numSet:
                while (ptr in numSet):
                    ptr += 1
                    counter += 1

            maxConsecutive = max(maxConsecutive, counter)
        
        return maxConsecutive