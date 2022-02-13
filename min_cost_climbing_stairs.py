def minCostClimbingStairs(cost):     
        if len(cost) == 1:
            return cost[0] #if cost[0] < cost[1] else cost[1]
        if len(cost) > 2:
            for i in range(2,len(cost)):
                cost[i] = cost[i] + min(cost[i-2], cost[i-1])
        
        # travel_cost = [0]*len(cost)
        # travel_cost[0] = cost[0]
        # travel_cost[1] = cost[1]
        # travel_cost[2] = cost[2]+cost[0]
        # for i in range(3, len(cost)):
        return cost[len(cost)-1] if cost[len(cost)-1] < cost[len(cost)-2] else cost[len(cost)-2]
            
print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))