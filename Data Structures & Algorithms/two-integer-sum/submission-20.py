class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # method:
        # initialize a dictionary where key: ideal number (target - curr number) & val: curr number index
        # iterate through the list 
        # if hit, return value of dict hit + current index (smaller index first)
        # if miss, add to dict

        # key: ideal number (target - current number)
        # val: current number's index
        myDict = {}

        for i in range(len(nums)):
            idealNum = target - nums[i]
            
            if nums[i] in myDict.keys():
                return [myDict[nums[i]], i]
            
            myDict[idealNum] = i

        return []