class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while(start<=end):
            mid = (start+end)//2
            if( target == sorted_nums[mid] ):
                return mid
            if( target > sorted_nums[mid] ):
                start = mid+1
            else:
                end = mid-1
        return -1
        
        