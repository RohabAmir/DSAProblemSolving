class Solution(object):
    def buildArray(self, nums):
        ans=[1]*len(nums) 
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        return ans    
r=Solution()
print(r.buildArray([0,1,2,3,4,5]))        