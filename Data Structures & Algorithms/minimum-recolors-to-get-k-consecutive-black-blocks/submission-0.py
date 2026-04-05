class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        r = len(blocks)
        l = 0
        min_change = float('inf')
        if k > len(blocks):
            return 0
        
        def numWhites(l,k):
            val = 0
            for i in range(l, k):
                if blocks[i] != 'B':
                    val += 1
            return val

        while l+k <= r:
            min_change = min(min_change, numWhites(l, l+k))
            l += 1
        
        return min_change