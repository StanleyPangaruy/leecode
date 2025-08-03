class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        a=""
        for i in range(numRows):
            for j in range(i,len(s),2*(numRows-1)):
                a+=s[j]
                if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                    a+=s[j+2*(numRows-1)-2*i]
        return a
    
if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = solution.convert(s, numRows)
    print(f"The converted string is: {result}")