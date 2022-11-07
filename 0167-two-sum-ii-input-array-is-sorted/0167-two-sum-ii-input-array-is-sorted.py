class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1
        while(numbers[s]+numbers[e]!=target):
            su = numbers[s]+numbers[e]
            if(su<target):
                s+=1
            else:
                e-=1
        return( [ s+1, e+1 ] )
                    
                    
        