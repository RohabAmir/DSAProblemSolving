class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[True]*len(candies) #creating a new boolean array of size equal to given array
        boolVal=True
        for i in range (len(candies)):
            max=candies[i]+extraCandies
            for j in range(len(candies)):
                if (i==j):
                    continue
                if(max<candies[j]):
                    boolVal=False
                    result[i]=boolVal
        return result
r=Solution()
print(r.kidsWithCandies([2,3,5,1,3],3))
        
        
        