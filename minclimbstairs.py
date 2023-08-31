#746. Min Cost Climbing Stairs

class Solution(object):
    def minCostClimbingStairs(self, cost):
        for idx in range(2,len(cost)):
            cost[idx] += min(cost[idx-1], cost[idx-2])
        return min(cost[-2], cost[-1])
