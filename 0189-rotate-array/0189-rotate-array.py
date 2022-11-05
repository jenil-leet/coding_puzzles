class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        for idx in range(n//2):
            tmp = nums[idx]
            nums[idx] = nums[n-1-idx]
            nums[n-1-idx] = tmp    
        
        for idx in range(k//2):
            tmp = nums[idx]
            nums[idx] = nums[k-1-idx]
            nums[k-1-idx] = tmp
        
        for idx in range((n-k)//2):
            tmp = nums[idx+k]
            nums[idx+k] = nums[-idx-1]
            nums[-idx-1] = tmp 
        
        