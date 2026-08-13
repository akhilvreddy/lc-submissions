class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rMax = -1

        for i in range(len(arr)-1, -1, -1):
            rMax, arr[i] = max(arr[i], rMax), rMax

        return arr

        