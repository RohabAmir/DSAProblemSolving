class Solution(object):
    def largestOddNumber(self, num):
        n=len(num)-1 #we will check the last index of the string
        while(n>0):
            if(int(num[n]) %2 !=0): #no is odd
                return num[0:n+1] #return the whole number as a string
            else: #no is even
                n-=1
        if(n==0): #the rightmost integer
            if(int(num[n]) %2 !=0): #no is odd
                return num[0] 
            else: #even
                return "" #empty string
            
