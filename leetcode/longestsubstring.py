#Given a string s, find the length of the longest substring without repeating characters.
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
approach: Optimised window
two pointer left and right traversing using right and using left as and when we get a duplicate

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mp={}#using dict as a map for storing the indices of the elements in the string
        counter=0
        mx=0
        left_pointer=right_pointer=0

        #traversing from left to right 
        while right_pointer < len(s) :

            #if not exits in map add it to check later
            if mp.get(s[right_pointer],-1) == -1:
                counter+=1
                mp[s[right_pointer]]=right_pointer

            #if exits then check if it included in the current string(right-left+1) under consideration 
            #then update left to the indice of the next element
            elif mp.get(s[right_pointer]) >= left_pointer:
                left_pointer=mp[s[right_pointer]]+1
                mp[s[right_pointer]]=right_pointer
                counter=right_pointer - left_pointer + 1

            #not under consideration so just update the map 
            else :
                counter=right_pointer - left_pointer + 1
                mp[s[right_pointer]]=right_pointer
            mx=max(mx,counter)
            right_pointer+=1
        return mx
        