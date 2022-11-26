class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for i in nums1:
            nums1_dict[i] = nums1_dict.get(i, 0)+1
        nums3 = []
        for j in nums2:
            if(nums1_dict.get(j, 0) > 0):
                nums3.append(j)
                nums1_dict[j] = nums1_dict.get(j, 0) - 1
        return(nums3)