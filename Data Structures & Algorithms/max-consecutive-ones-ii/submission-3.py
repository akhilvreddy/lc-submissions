class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroInd = -1
        res = 0
        l = 0

        for i, n in enumerate(nums):
            if n == 0:
                if zeroInd >= 0:
                    res = max(res, i-l)
                    l = zeroInd + 1
                zeroInd = i

        print(l)
        return max(res, len(nums)-l)


        