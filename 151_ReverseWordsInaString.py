class Solution(object):
    def reverseWords(self, s):
        result="" #new resulted string
        i=0 #loop for getting the first letter
        n=len(s) #lenghth of given string
        while(i<n):
            while(i<n and s[i]==' '):
                i+=1
            if i>=n:
                break

            j=i+1 #For getting first space
            while(j<n and s[j]!=' '):
                j+=1

            word=s[i:j]
            if len(result)==0:
                result=word
            else: #to get the string in reverse order
                result = word + " " + result
            i=j+1 


        return result



