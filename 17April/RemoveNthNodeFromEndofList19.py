class ListNode:
    def __init__(self,val=None,next=None):
        self.next=next
        self.val=val

def removeNthFromEnd(head,n):
    temp = head
    count = 0
    while temp is not None:
        count +=1
        temp=temp.next
    steps = count - n
    if steps == 0:
        return head.next
    temp=head
    for _ in range(steps-1):
        temp=temp.next
    temp.next=temp.next.next
    return head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(5)

print("Original List:")
printList(head)

# Remove the 2nd node from the end (removes 4)
head = removeNthFromEnd(head, 2)

print("After removing 2nd node from end:")
printList(head)