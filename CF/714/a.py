t=int(input(""))
while t>0:
    n,k=map(int,input("").split(" "))
    # print(n,k)
    m=(n-1)//2
    # print("m is",m)
    if n==0 or n==1 or n==2:
        if k==0:
            ans=[i for i in range(n+1)]
            print(" ".join(map(str,ans[1:])))
        else :
            print("-1")
    elif m>=k:
        ans=[str(i) for i in range(n+1)]
        ans=ans[1:]
        # print("ans",ans)
        itr=1
        while k:
            ans[itr],ans[itr+1]=ans[itr+1],ans[itr]
            k-=1
            itr=itr+2
        # pass
        pt=" ".join(map(str,ans))
        print(pt)
        # for i in ans:
        #     print(i)
    else:
        print("-1")
    t=t-1
    
    
    
    
    # if n==1 :
    #     if k>=1:
    #         print("-1")
    #     else:
    #         print("1")
    #     # pass
    # elif n%2==0:
    #     m=0
    #     if n==2:
    #         if(k==0):
    #             print("1 2")
    #         else:
    #             print("-1")
    #     else:
    #         m=
    #         if()


    # elif n%2==1:
        
    #     pass
    # t=t-1


# while t>0:
#     a,b=map(int,input("").split(" "))
#     print(a,b)
#     #if a is 1/2
#     if a==1 or a==2 or b == a or b>a/2:
#         print("-1")
#         continue
#     # elif if :
#     else:
#         m=0
#         if (a-2)%2==0 :
#             m=(a-2)/2
#         else:
#             m=(a-2)/2 + 1
#         if(m<=b):
#             temp=b-1
#             ans = []
#             ans.append(1)
#             tp = 0
#             for i in range(a+1,b):
#                 if tp==0:
#                     ans.append(i+1)
#                     tp=1
#                 else:
#                     ans.append(i-1)
#                     tp=0
#                 # pass
#             ans.append(b)
#             pass
#         else:
#             print("-1")
#     t=t-1