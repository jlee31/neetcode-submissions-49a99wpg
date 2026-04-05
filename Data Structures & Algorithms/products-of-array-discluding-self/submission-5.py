class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        hasZero = False
        n = len(nums)
        ret = [0] * n
        numZero = 0

        for i in range(n):
            if nums[i] != 0:
                total = total * nums[i]
            if nums[i] == 0:
                hasZero = True
                numZero += 1    

        for i in range(n):
            if hasZero:
                if nums[i] != 0:
                    ret[i] = 0
                if nums[i] == 0:
                    if numZero >= 2:
                        ret[i] = 0
                    else:
                        ret[i] = total

            else:
                if nums[i] != 0:
                    ret[i] = total // nums[i]
            
        
        return ret

        # o(n) but uses integer division