# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch( s: str, p: str) -> bool:
        if (s == p):
            return (True)
        return (False)
    
def main():
    s = "aa"
    p = "a*"
    result = False
    result = Solution.isMatch(s, p)
    print (result)