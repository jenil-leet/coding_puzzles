class Solution {
public:
    
    bool containsDuplicate(vector<int>& nums) {
        std::map<int,int> nums_map;
        int num, i;
        for(i=0; i<nums.size(); i++)
        {    
            num = nums[i];
            if(nums_map.count(num)){
                return(true);
            }
            else
            {
                nums_map.insert({num, 1});
            }
        }
        return(false);
    }
};