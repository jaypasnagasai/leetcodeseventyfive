#2336. Smallest Number in Infinite Set

class SmallestInfiniteSet:

    def __init__(self):
        self.min_val = 1
        self.is_val_in_heap = {}
        #self.is_val_in_heap = set()
        self.heap = []
        heapify(self.heap)

    def popSmallest(self):
        if not self.heap:
            smallest = self.min_val
            self.min_val +=1
        else:
            smallest = heappop(self.heap)
            del self.is_val_in_heap[smallest]
            #self.is_val_in_heap.remove(smallest)
        
        return smallest

    def addBack(self, num):
        if num >= self.min_val or num in self.is_val_in_heap:
            return
        elif num == self.min_val - 1:
            self.min_val -= 1
        else:
            heappush(self.heap, num)
            self.is_val_in_heap[num] = True
            #self.is_val_in_heap.add(num)
