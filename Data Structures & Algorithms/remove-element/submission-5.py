class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1

        for i in range(len(nums)):
            while nums[j] == val and j >= 0:
                j -= 1
            
            if i >= j:
                return j + 1
            
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]


        return 0
        