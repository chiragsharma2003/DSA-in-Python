# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.

class Solution:
    
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root