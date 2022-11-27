class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if(m*n!=r*c):
            return(mat)
        flattened = [j for i in mat for j in i]
        reshaped = [flattened[c*i:c*(i+1)] for i in range(r)]
        return(reshaped)