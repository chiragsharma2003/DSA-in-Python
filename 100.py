# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not.
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

class Solution(object):
    def isSameTree(self, p, q):
        
        is_p_null = p is None
        is_q_null = q is None

        if is_p_null and is_q_null:
            return True
        elif is_p_null or is_q_null:
            return False
        else:
            status = p.val == q.val
            status &= self.isSameTree(p.left, q.left)
            status &= self.isSameTree(p.right, q.right)
            return status
        