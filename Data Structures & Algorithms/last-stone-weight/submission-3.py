class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # solution with loops
        # n log n solution

        

        while True:
            stones = sorted(stones)
            l = len(stones)
            if l == 0:
                return 0
            if l == 1:
                return stones[0]
            max1 = stones[l - 1]
            max2 = stones[l - 2]
            stones.append(abs(max1 - max2))
            stones.pop(l-1)
            stones.pop(l-2)