class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_arr = {num:idx for idx, num in enumerate(nums)}
        print(dict_arr)
        for idx, num in enumerate(nums):
            idx2 = dict_arr.get(target-num, -1)
            if(idx2!=-1 and idx2!=idx):
                return([idx, idx2])