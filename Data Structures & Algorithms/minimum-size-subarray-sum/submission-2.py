class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        l = 0
        res = len(nums)
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                res = min(res, r-l+1)
                curr -= nums[l]
                l += 1
        
        if sum(n for n in nums) < target:
            return 0
        else:
            return res




        