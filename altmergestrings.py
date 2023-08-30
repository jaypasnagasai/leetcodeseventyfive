# 1431. Kids With the Greatest Number of Candies

class Solution(object):
    def mergeAlternately(self, word1, word2):
        # Get the lengths of both input words
        m = len(word1)
        n = len(word2)
        
        # Initialize pointers for both words and an empty list to store the result
        i = 0
        j = 0
        result = []

        # Loop until we have processed all characters from both words
        while i < m or j < n:
            # Check if there are more characters in word1 to merge
            if i < m:
                result += word1[i]  # Add the current character from word1 to the result
                i += 1  # Move the pointer for word1 to the next character
            
            # Check if there are more characters in word2 to merge
            if j < n:
                result += word2[j]  # Add the current character from word2 to the result
                j += 1  # Move the pointer for word2 to the next character

        # Join the characters in the result list to form the merged string
        return "".join(result)
