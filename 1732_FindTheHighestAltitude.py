class Solution(object):
    def largestAltitude(self, gain):
        sum=0
        max=0
        for i in range(len(gain)):
            sum=sum+gain[i] #-5,-4,1,1,-6
            if(max<sum):
                max=sum
        return max
r=Solution()
print(r.largestAltitude([-5,1,5,0,-7]))