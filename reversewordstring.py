# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s):
        # Split the input string into a list of words and reverse it
        reversed_words = reversed(s.split())

        # Join the reversed words using a space as the separator
        reversed_sentence = ' '.join(reversed_words)

        # Return the reversed sentence
        return reversed_sentence
