class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        cur = []

        def backtrack(numOpen, numClose):
            if len(cur) == 2 * n:
                ret.append(''.join(cur))
                return
            
            if numOpen < n:
                cur.append('(')
                backtrack(numOpen+1, numClose)
                cur.pop()
            
            if numOpen > numClose:
                cur.append(')')
                backtrack(numOpen, numClose + 1)
                cur.pop()
        
        backtrack(0,0)

        return ret