class Solution(object):
    def restoreString(self, s, indices):
        shuffledString=[""]*len(s) #["","","","","","","",""]
        for i in range(len(indices)) :
            shuffledString[indices[i]]= s[i] 
        return "".join(shuffledString) #return the string list into a string 
r=Solution()
print(r.restoreString("codeleet",[4,5,6,7,0,2,1,3]))
            