class Solution(object):
    def sumZero(self, n):
        result=[1]*n  #creating array having n elements
        
        x = -(n/2) #for getting the first value of the resulted array
        
        for i in range(len(result)):
            
            if(n%2!=0): #If no is odd
                result[i]=x
                x+=1
                
            else: #if no is even
                if(i==n/2):
                    x+=1
                result[i]=x
                x+=1
            
        return result
        