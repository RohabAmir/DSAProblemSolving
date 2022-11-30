class Solution(object):
    def runningSum(self, nums):
        sum=0
        ans=[1]*nums #create a new array having size equal to nums arrays
        for i in range(len(nums)):
            sum= sum+nums[i]
            ans[i]=sum
        return ans
r=Solution()
print(r.runningSum([1,2,3,4]))