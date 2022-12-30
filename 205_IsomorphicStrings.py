lass Solution(object):
    def isIsomorphic(self, s, t):
#fisrt of all both strings required same lenght to get one-to-one mapping between them 
        if(len(s)!=len(t)):
            return False
#Now for mapping we need to create a dictionary in order to have a look that which character in a string is going to replace with
        mapST={} #creating a dictionary
        mapTS={}
        #map[keys]=values
        # for i in range(len(s)):
        #     char1=s[i]
        #     char2=t[i]
        for char1,char2 in zip(s,t):
#To detect if it already has another mapping
            if((char1 in mapST and mapST[char1] != char2) or
               (char2 in mapTS and mapTS[char2] != char1)):
               return False
            #Insertion 
            mapST[char1]=char2 #{ e:a , g:d , g:d}->mapST
            mapTS[char2]=char1 #{ a:e , d:g , d:g}->mapTS
        return True
