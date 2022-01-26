'''
find and print all the permutations of a string
we use recursive approach
we keep exchanging one index of the string with all the elements of the string and after this doing 
the same process for the index after this till all the elements have been exchanged
s= a b c
lvl1 call 
(a b c)     (b a c)     (c b a)
1 with 1    1 with 2    1 with 3
lvl2 call
(a b c and a c b)   (b a c and b c a)

if l==r i.e if we have set strings at all the indices print

after print reorder coz we have swaped the main string i.e from (a c b to (a b c) coz need 
this for the next branch or previous iteration
'''

def permute(s,l,r):
    if l==r:print(''.join(s))

    for i in range(l,r+1):
        s[l],s[i]=s[i],s[l]
        permute(s,l+1,r)
        s[l],s[i]=s[i],s[l]

    pass

if __name__=='__main__':
    print("hi")

    #strings are immutable in python therefore using list for the operations
    s=list("abc")
    permute(s,0,len(s)-1)