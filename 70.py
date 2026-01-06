# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top?

class Solution:
    def climbStairs(self, n):
        a,b = 1,0
        for _ in range(n):
            a,b = a+b,a
        return a