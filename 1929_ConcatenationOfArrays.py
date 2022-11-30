class Solution(object):
    def getConcatenation(self,nums):
#Sol;1
        ans1=[] 
        ans2=[]
        for i in range(len(nums)):
            ans1.append(nums[i])
        for i in range(len(nums)):
            ans2.append(nums[i])
        return ans1 + ans2
# Sol2;
        n=len(nums)
        ans=[2]*nums
        for i in range(len(nums)):
            ans[i]==nums[i]
            ans[i+n]==nums[i]
        return ans
r=Solution()
print(r.getConcatenation([1,2,1]))     
            
        
    
        
    
            