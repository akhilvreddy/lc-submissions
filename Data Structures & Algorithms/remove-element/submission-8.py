class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r: # come back to this
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        
        return r + 1

        