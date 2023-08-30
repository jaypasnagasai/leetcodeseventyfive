# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # Loop through the flowerbed array
        for i, flower in enumerate(flowerbed):
            # Check if the current spot is empty (flower == 0)
            # and if it's the first position or the previous position is also empty
            # and if it's the last position or the next position is also empty
            if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # Place a flower in the current spot
                flowerbed[i] = 1
                # Reduce the number of flowers left to be placed
                n -= 1
            # Check if the required number of flowers have been placed
            if n <= 0:
                # If enough flowers have been placed, return True
                return True

        # If we couldn't place enough flowers, return False
        return False
