import heapq

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # cache is map of key : (value, freq, recency)
        self.cache = {}

        # (freq, recency, key)
        self.heap = []
        self.time = 0
    
    def evict(self):
        while True:
            freq, rec, key = heapq.heappop(self.heap)
            if key in self.cache and freq == self.cache[key][1]:
                self.cache.pop(key)
                return
        
    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache:
            val, freq, rec = self.cache[key]
            self.cache[key] = (val, freq + 1, self.time)
            heapq.heappush(self.heap,(freq + 1, self.time, key))
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.cache:
            _, oldFreq, oldTime = self.cache[key]
            self.cache[key] = (value, oldFreq + 1, self.time)
        else:
            if len(self.cache) == self.capacity:
                self.evict()
            self.cache[key] = (value, 1, self.time)
            heapq.heappush(self.heap, (1, self.time, key))
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)