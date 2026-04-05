class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        l_heights = [0] * l
        r_heights = [0] * l
        r_wall = l_wall = 0
        ret = 0

        for i in range(l):
            j = -i - 1

            l_heights[i] = l_wall
            r_heights[j] = r_wall

            l_wall = max(height[i], l_wall)
            r_wall = max(height[j], r_wall)
            
        for i in range(l):
            pot = min(l_heights[i], r_heights[i])
            ret += max(0, pot - height[i])

        return ret