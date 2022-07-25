# Write a function "reverseParentheses" reverse the strings in each pair of matching parentheses, 
# starting from the innermost one.
class Solution(object):
    def reverseParentheses(s):
        if not s:
            return ''
        
        arr = []
        for char in s:
            if char == ')':
                combine_str = ''
                while arr and arr[-1] != '(':
                    elem = arr.pop()[::-1]
                    combine_str += elem
                arr.pop()
                arr.append(combine_str)
            else:
                arr.append(char)
        return "".join(arr)
s ="(biqas(-)sumjan ) "
print(Solution.reverseParentheses(s))