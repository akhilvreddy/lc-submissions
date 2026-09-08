class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, n in enumerate(nums):
            arr.append((n, i))
        
        arr.sort()
        i, j = 0, len(arr)-1
        while i < j:
            currSum = arr[i][0] + arr[j][0]
            if currSum > target:
                j-=1
            elif currSum < target:
                i+=1
            else:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]

        return []

        