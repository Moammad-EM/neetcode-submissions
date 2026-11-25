class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = ["" for i in range(capacity)]
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == len(self.arr):
            self.resize()
        self.length += 1
        self.arr[self.length -1] = n

    def popback(self) -> int:
        if self.length >= 1: 
            self.length -= 1
            return self.arr[self.length]

    def resize(self) -> None:
        self.arr += ["" for i in range(len(self.arr))]

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return len(self.arr)