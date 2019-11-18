# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:27:13 2019

@author: group
"""

class Solution(object):
    def __init__(self):
        self.stack = []
        self.final = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        self.stack.append(root)
        while len(self.stack) != 0:
            while root != None:
                self.stack.append(root)
                root = root.left
            root = self.stack.pop()
            self.final.append(root.val)
            root = root.right
        return self.final[:-1]