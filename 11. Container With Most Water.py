# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:26:51 2019

@author: group
"""
#Input: [1,8,6,2,5,4,8,3,7]
#Output: 49

#
#def maxArea(input_list):
#    result = 0
#    for i in range(len(input_list)):
#        for j in range(i+1, len(input_list)):
#            if (j - i)*min(input_list[i], input_list[j]) > result:
#                result = (j - i)*min(input_list[i], input_list[j])
#    return result
    





#def maxArea(input_list):
#    result = []
#    for i in range(len(input_list)):
#        result.append((i,input_list[i]))
#    dic = dict(result)
    
    
def maxArea(input_list):
    result = 0
    i = 0
    j = len(input_list)-1
    while(i < j):
        if (j - i)*min(input_list[i], input_list[j]) > result:
#            print(result)
            result = (j - i)*min(input_list[i], input_list[j])
        if input_list[i] > input_list[j]:
            j -= 1
        else:
            i += 1
    return result

a = [1,8,6,2,5,4,8,3,7]

maxArea(a)
            
    
        