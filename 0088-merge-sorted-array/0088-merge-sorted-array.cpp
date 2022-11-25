class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums3(m);
        int nums3idx = 0, nums2idx = 0, nums1idx = 0, i;
        for(i=0; i<m; i++)
            nums3[i] = nums1[i]; //copy over all elems
        while(nums3idx < m && nums2idx < n){
            if( nums3[nums3idx] < nums2[nums2idx] ){
                nums1[nums1idx] = nums3[nums3idx];
                nums3idx++;
            }    
            else{
                nums1[nums1idx] = nums2[nums2idx];
                nums2idx++;
            }
            nums1idx++;
        }
        while(nums3idx<m){
            nums1[nums1idx] = nums3[nums3idx];
            nums1idx++;
            nums3idx++;
        }
        while(nums2idx<n){
            nums1[nums1idx] = nums2[nums2idx];
            nums1idx++;
            nums2idx++;
        }
    }
};