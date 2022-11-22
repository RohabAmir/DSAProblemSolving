class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[1]*len(nums) #create a list of size(nums)
        for i in range(len(nums)):
            count=0
            max=nums[i] 
            for j in range(len(nums)):
                if(max>nums[j] and i is not j):
                    count+=1
            ans[i]=count
        return ans
r=Solution()
print(r.smallerNumbersThanCurrent([7,7,7,7]))                    