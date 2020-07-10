class HeapBuilder:
    def __init__(self):
        self._swaps = [] #array of tuples or arrays
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def swapup(self,i):
        if i !=0:
#             print(self._data[int((i-1)/2)], self._data[i])
            if self._data[int((i-1)/2)]> self._data[i]:
#                 print('2')
                self._swaps.append(((int((i-1)/2)),i))
                self._data[int((i-1)/2)], self._data[i] = self._data[i],self._data[int((i-1)/2)]
                self.swapup(int((i-1)/2))
    # so for i in range(0,n), implement swap up  ai < a2i+1  ai < a2i+2
        for i in range(len(self._data)-1,0,-1):
            self.swapup(i)
#             print('1')
#             for j in range(i + 1, len(self._data)):
#                 if self._data[i] > self._data[j]:
#                     self._swaps.append((i, j))
#                     self._data[i], self._data[j] = self._data[j], self._data[i]

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
