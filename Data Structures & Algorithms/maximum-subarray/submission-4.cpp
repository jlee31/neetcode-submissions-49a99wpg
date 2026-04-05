class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int totalMax = nums[0];
        int currMax = nums[0];
        int l = nums.size();
        for (int i = 1; i < l; i++) {
            currMax = max(nums[i], currMax + nums[i]);
            totalMax = max(currMax, totalMax);
        }
        return totalMax;
    }
};
