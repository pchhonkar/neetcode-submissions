class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        char_freq={}

        for i in range(len(s)):
            char_freq[s[i]]= 1+ char_freq.get(s[i],0)

        for i in range(len(t)):
            if t[i] not in char_freq:
                return False
            if char_freq[t[i]]==0:
                return False

            else:
                char_freq[t[i]]= char_freq.get(t[i],0)-1

        return True

        