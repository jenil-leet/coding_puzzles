class Solution:
    def generate_pascal_elem(self, pascal_last: list, j:int) ->List[int]:
        left = 0
        right = 0
        if(j-1 >= 0 ):
            left = pascal_last[j-1]
        if(j < len(pascal_last) ):
            right = pascal_last[j]
        return(left+right)
    def generate(self, numRows: int) -> List[List[int]]:
        row1 = [1]
        res = []
        res.append(row1)
        for i in range(1, numRows+1):
            res.append([self.generate_pascal_elem( res[-1], j ) for j in range(i)])
        return(res[1:])
            