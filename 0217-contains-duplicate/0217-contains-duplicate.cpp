class Solution {
public:
    
    bool containsDuplicate(vector<int>& nums) {
        std::map<int,int> nums_map;
        for(int i=0; i<nums.size(); i++)
            nums_map.insert({nums[i], 1});
        return(nums.size()!=nums_map.size());
    }
};