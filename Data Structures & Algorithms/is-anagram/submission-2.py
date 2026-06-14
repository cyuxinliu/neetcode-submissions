class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if len s not equal to len t return false
        for each char in the first string, check
        if it is in the second string. if it is in
        the second string, remove the char from the 
        second string to create a new string. then do 
        the next char of the first string
        """

        if len(s) != len(t): return False

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t[:j] + t[j+1:]
                    break
            else: # when i indented it one more time, it was wrong, why?
                return False 

        if t != "": return False

        return True                     



            