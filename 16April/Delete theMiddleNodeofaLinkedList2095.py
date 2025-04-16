class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head):
        if head.next==None:
            return None
        fast=head
        slow=head
        pre=slow
        while fast!=None and fast.next!=None:
            pre=slow
            fast=fast.next.next
            slow=slow.next
        pre.next=pre.next.next
        return head
    

def build_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print("->".join(map(str, vals)))

# Example
lst = [1, 2, 3, 4, 5]
head = build_linked_list(lst)
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.deleteMiddle(head)

print("After deleting middle:")
print_linked_list(new_head)