class Solution:
    def isValid(self, s: str) -> bool:
        open_b = ['{', '(', '[']
        close_b = ['}', ')', "]"]
        stack = []

        for value in s:
            if value in open_b:
                stack.append(value)
            if value in close_b:
                if stack == []:
                    return False
                if value == '}' and stack[-1] == '{':
                    stack.pop()
                elif value == ')' and stack[-1] == '(':
                    stack.pop()
                elif value == ']' and stack[-1]  == '[':
                    stack.pop()
                else:
                    return False

        return stack == []