class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        // Initialize maxSum...
        int maxSumSoFar = 0;
        // Traverse all the element through the loop...
        for(int i = 0; i < nums.size(); i++){
            // Keep adding the current value...
            maxSumSoFar += nums[i];
            // Update maxSum to maxSum and maxSumSoFar...
            if(maxSum < maxSumSoFar){
                maxSum = maxSumSoFar;
            }
            // if maxSumSoFar is less than 0 then update it to 0...
            if(maxSumSoFar < 0){
                maxSumSoFar = 0;
            }
        }
        return maxSum;      // Return the contiguous subarray which has the largest sum...
    }
};