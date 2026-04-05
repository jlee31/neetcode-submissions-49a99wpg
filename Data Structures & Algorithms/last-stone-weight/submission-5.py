import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using a heap
        # creating a maxHeap
        l = len(stones)
        for i in range(l):
            stones[i] *= -1

        heapq.heapify(stones) # o(n) time

        while len(stones) > 1:
            l1 = heapq.heappop(stones)
            l2 = heapq.heappop(stones)
            if l1 != l2:
                heapq.heappush(stones, l1 - l2)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0