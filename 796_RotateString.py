class Solution(object):
    def rotateString(self, s, goal):
#Solution 1:
        # if( len(s)==len(goal) and goal in s+s):
        #     return True
        # else:
        #     return False
#Solution 2:
        if (s==goal): #if both strings contain same letters
            return True
        for i in range(1,len(s)):
            temp = s[i:] + s[:i]
            if(temp==goal):
                return True
        return False