#875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles, H):
        max_val = max(piles)
        l = 1
        h = max_val
        
        while l <= h:
            mid = l + (h - l) // 2
            if self.calculate_sum(piles, mid) > H:
                l = mid + 1
            else:
                h = mid - 1
                
        return l
    
    def calculate_sum(self, piles, speed):
        total_time = 0
        for pile in piles:
            total_time += (pile + speed - 1) // speed
        return total_time
