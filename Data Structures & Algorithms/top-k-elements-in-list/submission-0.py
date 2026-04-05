class Solution:
    def topKFrequent(self, nums, k):
        hmap = {}   # value : count
        out = []

        # count frequencies
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1

        sorted_keys = sorted(hmap, key=lambda x: hmap[x], reverse=True)

        for i in range(k):
            out.append(sorted_keys[i])

        return out
