class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort()
        res = 1
        time = (target - arr[-1][0]) / arr[-1][1]
        
        for p, s in arr[::-1]:
            currTime = (target - p) / s
            if currTime > time:
                res += 1
                time = currTime

        return res



        