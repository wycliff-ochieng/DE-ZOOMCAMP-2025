class Solution:
    def merge_alternately(self,word1:str,word2:str)->str:
        A,B = len(word1),len(word2)
        a,b = 0,0
        word = 1
        s = []

        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a+=1
            else:
                s.append(word2[b])
                b+=1
        
        while a < A:
            s.append(word1[a])
            a+=1

        while b < B:
            s.append(word2[b])
            b+=1

        return ''.join(s) 
    
#words = Solution('abcd','pqr')
    print(merge_alternately('abcd','qrs'))