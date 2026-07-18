from collections import defaultdict
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        heap = []

        for i in range(k):
            counts[nums[i]] += 1
            heapq.heappush(heap, -nums[i])
        
        
        res = []
        l, r = 0, k-1
        print(heap)

        while r < len(nums):
            while heap and not counts[-heap[0]]: 
                heapq.heappop(heap)
            
            res.append(-heap[0])
            l, r = l + 1, r+1
            if r != len(nums):
                counts[nums[l-1]] -= 1
                counts[nums[r]] += 1
                heapq.heappush(heap, -nums[r])
        
        return res


        
