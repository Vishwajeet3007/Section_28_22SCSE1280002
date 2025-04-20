class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if head==None or head.next==None or head.next.next==None:
            return head
        oddHead = head
        evenHead =  head.next
        evenStart = evenHead
        while evenHead!=None and evenHead.next!=None:
            oddHead.next = oddHead.next.next
            evenHead.next = evenHead.next.next

            oddHead = oddHead.next
            evenHead = evenHead.next
        oddHead.next=evenStart
        return head
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test the function
arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.oddEvenList(head)

print("Rearranged Linked List (Odd-Even):")
print_linked_list(new_head)