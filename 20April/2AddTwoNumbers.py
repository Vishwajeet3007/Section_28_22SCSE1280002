class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = ListNode()
        new = dummyNode
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            new.next = ListNode(val)
            new = new.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyNode.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# 🔍 Test Case Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

print("Input Linked List 1:")
print_linked_list(l1)

print("Input Linked List 2:")
print_linked_list(l2)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Result Linked List:")
print_linked_list(result)
