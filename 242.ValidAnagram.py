class Solution(object):
    def isAnagram(self, s, t):
        # return sorted(s)==sorted(t)
        # return Counter(s)==Counter(t)
        if(len(s)!=len(t)):
            return False
        countS,countT={},{}

        for i in range(len(s)): #for counting letters 
            countS[s[i]]= 1 + countS.get(s[i],0)
            countT[t[i]]= 1 + countT.get(t[i],0)
        for char in countS: #for comparing characters
            if countS[char]!=countT.get(char,0):
                return False
        return True