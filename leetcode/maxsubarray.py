'''
https://leetcode.com/problems/maximum-subarray/
Kadane's algorithm
imp:to refresh the current counting variable to 0 if the adding current value makes it negative

'''
import sys
def maxSubArray(self, nums):
    current_max=0
    max_till_now=-sys.maxint - 1

    for i in nums:
        current_max+=i
        
        if current_max > max_till_now:
            max_till_now=current_max
            
        if current_max<0:
            current_max=0
        
    
    return max_till_now
    