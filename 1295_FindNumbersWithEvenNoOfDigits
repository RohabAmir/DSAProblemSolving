class Solution(object):
    def findNumbers(self, nums):
        count=0 #checks the even no of digit in the given array
        for number in nums: #iterate over input list
            digits=0 #it will counts the no of digits
            while(number>0):
                number /= 10
                digits +=1 #2,3,1,1,4
            if(digits%2 == 0):
                count+=1 #2
        return count
        