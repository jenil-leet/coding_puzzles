class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        ret_arr = []
        sq_nums = [i*i for i in nums]
        while( start<= end ):
            # print( sq_nums[start], sq_nums[end] )
            if(sq_nums[start]<sq_nums[end]):
                ret_arr = [sq_nums[end]] + ret_arr
                end -= 1
            else:
                ret_arr = [sq_nums[start]] + ret_arr
                start += 1
            
        return(ret_arr)