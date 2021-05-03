'''
https://leetcode.com/problems/add-two-numbers/
approach : iterate two list and maintain a buffer for carry 
take special care or 3 cases
1.list one is smaller
2.list two is smaller
3.last number as a carry so make node of this number 

'''
class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rn=ListNode()
        head=rn
        buffer=0
        while l1!= None or l2!=None:
            rn.val=(l1.val+l2.val +buffer)%10 #get the units value
            buffer=(l1.val+l2.val +buffer)/10 #carry 
            
            if l1.next ==None and l2.next==None and buffer!=0:
                rn.next=ListNode(buffer)
                return head
            elif l1.next ==None and l2.next==None:
                return head
            elif l1.next == None:
                while l2.next != None:
                    tempval=(l2.next.val+buffer)%10
                    buffer=(l2.next.val+buffer)/10
                    temp =ListNode(tempval)
                    rn.next=temp
                    rn=temp
                    l2=l2.next
            elif l2.next ==None :
                while l1.next!=None:
                    print(l1.next.val,"-")
                    tempval=(l1.next.val+buffer)%10
                    buffer=(l1.next.val+buffer)/10
                    temp =ListNode(tempval)
                    rn.next=temp
                    rn=temp
                    l1=l1.next
            l1=l1.next
            l2=l2.next
            if l1 == None and l2 ==None and buffer!=0:
                rn.next=ListNode(buffer)
                return head
            elif l1 == None and l2 ==None:
                continue
            rn.next=ListNode()
            rn=rn.next
        return head
            