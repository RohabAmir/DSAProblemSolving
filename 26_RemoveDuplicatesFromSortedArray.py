class Solution(object):
    def removeDuplicates(self, nums):
        if (len(nums)==0): #Condition if there is an empty list
            return 0
        length=1 #it will count the distinct elements 
        prev=nums[0]
        index=1 #it will alter the input list
        for i in range(1,len(nums)):
        #checking for the elements which are not duplicate 
            if(nums[i]!=prev):
                length+=1 #incrementing the length of array
                prev=nums[i] #changing the position of previous value
                nums[index]=nums[i] #for each iteration altering the given list
                index+=1
        return length 
        
r=Solution()
print(r.removeDuplicates([1,1,1,2,2,3,3,3,3,4,5,5,6,6,7,7,7,8,9,9]))