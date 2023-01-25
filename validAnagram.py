def isAnagram(self, s, t):
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        :type s: str
        :type t: str
        :rtype: bool

        RUNTIME
        Beats 94.18%
        
        MEMORY
        Beats 93%
        """

        dict1 = {}
        dict2 = {}

        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1
        
        for letter in t:
            if letter in dict2:
                dict2[letter] += 1
            else:
                dict2[letter] = 1
        
        if dict1 == dict2:
            return True
        else:
            return False