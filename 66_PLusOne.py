class Solution(object):
    def plusOne(self, digits):
        
#coversion of array having digits into an integer by using list comprehension method 
#Reversing the list to get the unit part and then yield each number multiplies by 10 to the power of its positin in the array.

        Integer=sum(e * 10 ** i for i,e in enumerate(digits[::-1]))
        result=Integer + 1 
        
#Converting back the integer into an array of digits 

        return [ int(x) for x in str(result) ]
r=Solution()
print(r.plusOne([9,9,9]))