'''
https://leetcode.com/problems/two-sum/
find distinct indices whoes sum is given

trick:distinct indices not same 
eg [3,3] would have answer 1,2 when target is 6
but for [3] would not satisfy req

'''
class Solution(object):
    def twoSum(self, nums, target):

        #empty haven't already stored the numbers which exits coz need only numbers which are distinct 
        mp=dict()
        for i,v in enumerate(nums):
            rq=target-v

            #not checking val because its already present in the list we only need to check target - val
            if mp.get(rq,-1) != -1 :
                return i, mp[rq]

            #adding after checking so that we do not use the same element twice 
            else:
                mp[v]=i
        
