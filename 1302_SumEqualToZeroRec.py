class Solution(object):
    def sumZeroRec(self,n,result,i,v): 
        # base condition :
        if(i>=n):
            return 
        else:

            if(n%2!=0):#No is odd
                result[i]=v
            else: #No is even
                if(i==n/2): #eliminate zero
                    v-=1
                result[i]=v
            self.sumZeroRec(n,result,i+1,v-1)
            return result
    def sumZero(self, n):
        result=[1]*n
        return self.sumZeroRec(n,result,0,n/2)
       