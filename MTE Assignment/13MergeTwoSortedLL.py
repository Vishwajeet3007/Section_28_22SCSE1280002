class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def mergeTwoSortedLL(l1:ListNode,l2:ListNode) ->ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    result = None
    if l1.val < l2.val:
        result = l1
        result.next = mergeTwoSortedLL(l1.next,l2)
    else:
        result = l2
        result.next = mergeTwoSortedLL(l1,l2.next)
    return result

def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Test Example
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])

merged = mergeTwoSortedLL(l1, l2)

print("Merged Linked List:")
print_linked_list(merged)


