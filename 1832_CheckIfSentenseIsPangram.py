class Solution(object):
    def checkIfPangram(self, sentence):
        if(len(set(sentence)))==26:
            return True
        else:
            return False
r=Solution()
print(r.checkIfPangram("qwerttyuioplkmjnhhgbvfdcxsaz"))