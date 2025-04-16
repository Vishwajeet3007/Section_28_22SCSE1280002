class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
def reverseLL(head):
    if not head or not head.next:
        return head
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_from_middle(head):
    mid = reverseLL(head)
    while mid:
        print(mid.val, end=" ")
        mid = mid.next
    print() 


head = create_linked_list([1, 2, 3, 4, 5,7,9])
print_from_middle(head)  


head = create_linked_list([1, 2, 3, 4, 5, 6])
print_from_middle(head)  
