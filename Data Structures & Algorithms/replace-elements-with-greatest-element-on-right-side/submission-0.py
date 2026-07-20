class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = -1
        res = [0]*len(arr)

        for i in range(len(arr)-1, -1, -1):
            res[i] = num
            num = max(num, arr[i])

        return res
        