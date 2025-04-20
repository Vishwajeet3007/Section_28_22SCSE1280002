class ListNode:
    def __init__(self,val = None,next=None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def deleteAllKeyInDLL(self,head,key):
        temp = head
        while temp:
            new_node = temp.next
            if temp.val == key:
                if temp.prev is None:
                    head = temp.next
                    if head:
                        head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
            
            temp = new_node
        return head
def print_dll(head):
    while head:
        print(head.val, end=" <-> " if head.next else "\n")
        head = head.next


# Create DLL: 2 <-> 2 <-> 3 <-> 2 <-> 4
n1 = ListNode(10)
n2 = ListNode(4)
n3 = ListNode(10)
n4 = ListNode(10)
n5 = ListNode(6)

n1.next, n2.prev = n2, n1
n2.next, n3.prev = n3, n2
n3.next, n4.prev = n4, n3
n4.next, n5.prev = n5, n4

head = n1
sol = Solution()
new_head = sol.deleteAllKeyInDLL(head, 10)

print_dll(new_head)  
