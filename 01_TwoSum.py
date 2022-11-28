class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)): #iterate array with i
            for j in range(len(nums)):  #iterate array with j
                if nums[i]+nums[j] == target and i is not j:
                    return[i,j]
                