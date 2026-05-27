class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:

            encoded += str(len(i)) + "#"+ i

        return encoded
       

        

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0

        while i<len(s):
            j=s.index("#", i)
            length=int(s[i:j])
            z= s[j+1: j+1+ length]
            decoded.append(z)
            i=j+1+length 

        return decoded
        
        
