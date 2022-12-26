class Solution(object):
    def removeOuterParentheses(self, s):
        openBracket=0
        closeBracket=0
        sIndex=0
        innerBracketsString=""
        for index in range(len(s)):
            if s[index]=='(':
                openBracket +=1
            else:
                closeBracket +=1
            if openBracket == closeBracket:
                innerBracketsString = innerBracketsString+s[sIndex+1:index]
                sIndex=index+1
                openBracket=0
                closeBracket=0
        return innerBracketsString
            