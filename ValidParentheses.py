Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Solution:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str ##if p is not opening bracket it has open bracket in stack and lookup set or not.
        :rtype: bool
        """
        stack=[] ## define a stack
        lookup={')':'(','}':'{',']':'['} ## mapping the closed to open brackets. 
        for p in s:
            if p in lookup.values(): #Here we check p is opening bracket or not
                stack.append(p)      # if openning then we put in stack.
            elif stack and lookup[p]==stack[-1]:#check if p is not opening bracket it
                                        #has bracket in stack and lookup maching set or not.
                stack.pop() 
            else:
                return False
        return stack==[] ##Here we check stack is empty or not.
