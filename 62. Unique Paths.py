# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 23:07:14 2019

@author: group
"""

class Solution:
    
    def decrementMultiply(self, start: int, end: int) -> int:
        res = 1
        
        for n in range(start, end - 1, -1):
            res *= n
        
        return res
    
    def uniquePaths(self, m: int, n: int) -> int:
        total = m - 1 + n - 1
        div = self.decrementMultiply(total, total - (n - 1 - 1))
        denom = self.decrementMultiply(n - 1, 1)
        
        return int(div / denom)