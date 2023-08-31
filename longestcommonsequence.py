#1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, s, t):
        prev=[0 for i in range(len(t)+1)] 
        curr=[0 for i in range(len(t)+1)]
        
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):

                if s[i-1]==t[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev=curr[:]

        return prev[len(t)]
