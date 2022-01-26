from sys import stdin, stdout
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))

class Listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

print("input number to add in linkedlist")
a=[0,1,2,3,4,5]
head=Listnode(a[0])
cur=head

for i in a[1:]:
    temp=Listnode(i)
    cur.next=temp
    cur=temp

print("trying to iterate the linkedlist")

temp=head
while temp!=None:
    print("->",temp.val)
    temp=temp.next


