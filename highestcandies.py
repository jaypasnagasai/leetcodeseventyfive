# 1431. Kids With the Greatest Number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Find out the greatest number of candies among all the kids.
        maxCandies = max(candies)
        
        # For each kid, check if they will have the greatest number of candies
        # among all the kids after adding the extra candies.
        result = []
        for i in range(len(candies)):
            # Compare the total candies the current kid will have with the
            # greatest number of candies overall.
            result.append(candies[i] + extraCandies >= maxCandies)
        
        return result
