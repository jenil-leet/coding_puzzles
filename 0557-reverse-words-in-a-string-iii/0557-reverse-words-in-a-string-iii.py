class Solution:
    def reverseWords(self, s: str) -> str:
        idx = 0
        n = len(s)
        ret_s = ""
        word = ""
        while(idx<n):
            char = s[idx]
            if(char!=" "):
                word = char+word
            else:
                ret_s += ( word + char )
                word = ""
            idx+=1
        ret_s+=word
        return(ret_s)
        