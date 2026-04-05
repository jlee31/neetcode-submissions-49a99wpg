class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # solution with loops
        # n^2 log n solution
        # this one is even worse cuz we have to sort everytime

        while True:
            stones = sorted(stones)
            l = len(stones)
            if l == 0:
                return 0
            if l == 1:
                return stones[0]
            max1 = stones[l - 1]
            max2 = stones[l - 2]
            if abs(max1 - max2) != 0:
                stones.append(abs(max1 - max2))
            stones.pop(l-1)
            stones.pop(l-2)