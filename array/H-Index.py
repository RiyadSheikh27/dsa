class Solution:
    def __init__(self, arr):
        self.list = arr
        n = len(self.list)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]

        h = 0
        for i in range(n):
            if self.list[i] >= n - i:
                h = n - i
                break

        self.h = h
        print(self.h) 


obj = Solution([3,0,6,1,5])

