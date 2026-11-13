class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sets = set(nums)

        if len(nums) < 2: return len(nums)
        count = 1
        for num in sets:
            if(num-1) not in sets:
                length = 1
                while(num+length) in sets:
                    length += 1
                count = max(count,length)

        return count
