class Solution(object):
    def longestCommonPrefix(self, strs):
        result=[]
        #sort the given array
        strs.sort()
#Now get the first and last strings
        first=strs[0]
        last=strs[len(strs)-1]
#Start comparing each letter
        for i in range(len(first)):
            if(first[i] != last[i]):
                break
            result.append(first[i]) #["f","l"]

        longestCommonPrefix="".join(result) #"fl"
        return longestCommonPrefix