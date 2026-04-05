class Solution {
public:

    int findMin(vector<int> &nums) {
        int min = 1000000;
        int len = nums.size();
        for (int i = 0; i < len; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
        }
        return min;
    }
};
