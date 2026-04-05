class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles = sorted(piles)
        lo = 1
        hi = max(piles)
        k = hi

        # checking if koko can finish at mid
        while lo < hi:
            tmp_hours = 0
            mid = (lo + hi) // 2
            for pile in piles:
                tmp_hours += (pile + mid - 1) // mid
            if tmp_hours <= h:
                k = mid
                hi = mid
            else:
                lo = mid + 1
            

        return k
                

        
