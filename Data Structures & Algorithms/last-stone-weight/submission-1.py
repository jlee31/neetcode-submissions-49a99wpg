class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # solution 1 with loops
        while True:
            l = len(stones)
            # if l == 0:
            #     return 0
            if l == 1:
                return stones[0]

            max1_idx = 0
            for i in range(l):
                if stones[i] > stones[max1_idx]:
                    max1_idx = i

            max2_idx = 0 if max1_idx != 0 else 1

            for i in range(l):
                if i != max1_idx and stones[i] > stones[max2_idx]:
                    max2_idx = i
            
            high = max(max1_idx, max2_idx)
            low = min(max1_idx, max2_idx)
            stones.append(abs(stones[max1_idx] - stones[max2_idx]))

            stones.pop(high)
            stones.pop(low)