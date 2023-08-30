#1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1, word2):
        # Initialize frequency lists for each letter in the alphabet
        lst1 = [0] * 26
        lst2 = [0] * 26
        
        # Count the occurrences of each letter in word1
        for i in word1:
            lst1[ord(i) - 97] += 1
        
        # Count the occurrences of each letter in word2
        for i in word2:
            lst2[ord(i) - 97] += 1
        
        # Check if the sets of letters present are the same in both words
        for i in range(26):
            # If one word has a letter while the other doesn't, they can't be close
            if (lst1[i] > 0 and lst2[i] == 0) or (lst1[i] == 0 and lst2[i] > 0):
                return False
        
        # Sort the frequency lists
        lst1.sort()
        lst2.sort()
        
        # Check if the sorted frequency lists are the same
        if lst1[:] == lst2[:]:
            return True
        else:
            return False
