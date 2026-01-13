# 3453. Separate Squares I
# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] 
# represents the coordinates of the bottom-left point and the side length of a
# square parallel to the x-axis.
# Find the minimum y-coordinate value of a horizontal line such that the total 
# area of the squares above the line equals the total area of the squares below
# the line.
# Answers within 10-5 of the actual answer will be accepted.
# Note: Squares may overlap. Overlapping areas should be counted multiple times.

class Solution(object):
    def separateSquares(self, squares):
        
        def helper(mid):
            below_a = 0
            for x,y,l in squares:
                top = y+l
                if mid>=top:
                    below_a += l*l
                elif mid<y:
                    continue
                else:
                    below_a += l*(mid-y)
            return below_a

        up = float(max([s[1]+s[2] for s in squares]))
        down = float(min([s[1] for s in squares]))
        total_a = float(sum([s[2]**2 for s in squares]))
        target = total_a/2.0
        eps = 10**-5
        # print(up,down)
        while up-down>eps:
            mid = (up+down)/2
            below_a = helper(mid)
            if below_a<target:
                down = mid
            else:
                up = mid
        return up