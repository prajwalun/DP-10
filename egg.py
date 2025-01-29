# The superEggDrop method calculates the minimum number of attempts needed to find the critical floor 
# in the worst case using `k` eggs and `n` floors.

# Recursive Approach:
# - Base cases:
#   - If there are no floors or only one floor, return the number of floors (`f`).
#   - If there is only one egg, return `f` (must try every floor).
# - For each floor:
#   - Simulate dropping the egg and recursively calculate:
#     - If the egg breaks (`e-1` eggs, `k-1` floors below).
#     - If the egg doesn't break (`e` eggs, `f-k` floors above).
#   - Take the maximum of both cases (worst-case scenario) and add 1 (current drop).
#   - Track the minimum number of drops across all floors.

# TC: O(2^f) - Exponential due to recursive calls for each floor.
# SC: O(f) - Space for the recursion stack.


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return self.solve(k,n)
    
    def solve(self,e,f):
        if f == 0 or f == 1:
            return f
        if e == 1:
            return f
        
        ans = float('inf')
        
        for k in range(1,f):
            temp = 1 + max(self.solve(e-1,k-1), self.solve(e,f-k))
            ans = min(ans,temp)
            
        return ans