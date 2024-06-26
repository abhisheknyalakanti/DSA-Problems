class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
         final_cost = 0
         for cost_a, cost_b in costs:
            final_cost += cost_a
         costs.sort(key = lambda x : x[1] - x[0])
         for i in range(len(costs)//2):
            cost_a, cost_b = costs[i]
            final_cost += cost_b - cost_a
         return final_cost