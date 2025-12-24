# 3074 Apple Redistribution into Boxes
# You are given an array apple of size n and an array capacity of size m.
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well,
# and the ith box has a capacity of capacity[i] apples.
# Return the minimum number of boxes you need to select to redistribute these n packs of 
# apples into boxes.
# Note that, apples from the same pack can be distributed into different boxes.


class Solution(object):
    def minimumBoxes(self, apple, capacity):

        total_apples = sum(apple)
        capacity.sort(reverse=True)  # Sort in descending order
        used_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            if used_capacity >= total_apples:
                break
            used_capacity += cap
            boxes_used += 1
        
        return boxes_used