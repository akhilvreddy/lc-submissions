class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [-1]*capacity


    def get(self, i: int) -> int:
        return self.arr[i]



    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        self.arr[self.size-1] = n



    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

 

    def resize(self) -> None:
        self.arr.extend([-1]*self.capacity)
        self.capacity *= 2



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
