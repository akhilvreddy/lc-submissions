class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def curr_h(k):
            sum = 0
            for p in piles:
                sum += math.ceil(p / k)
            
            return sum

        lo, hi = 1, max(piles)
        res = max(piles)

        while lo <= hi:
            mid = (lo + hi)//2

            if curr_h(mid) > h:
                lo = mid + 1
            elif curr_h(mid) <= h:
                res = min(mid, res)
                hi = mid - 1
            else:
                return mid
        
        return res

        