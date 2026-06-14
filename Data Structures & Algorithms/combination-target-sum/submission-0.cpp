class Solution {
public:
    void combinationSumHelper(vector<int>& nums, int target, vector<vector<int>>& results, vector<int>& soFar, int start) {
        if (target == 0) {
            results.push_back(soFar);
            return;
        } else if (target < 0) {
            return;
        } else {
            for (int i = start; i < nums.size(); i++) {
                soFar.push_back(nums[i]);
                combinationSumHelper(nums, target - nums[i], results, soFar, i);
                soFar.pop_back();
            }
        }    
    }
    
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> results;
        vector<int> soFar;
        combinationSumHelper(nums, target, results, soFar, 0);
        return results;
    }
};