class ListNode:
    def __init__(self,val = None,next=None):
        self.val = val
        self.next = next
class Solution:
    def sizeOfLL(self,head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count
    def InstersectionPointOfTwoLL(self,headA,headB):
        sizeA = self.sizeOfLL(headA)
        sizeB = self.sizeOfLL(headB)
        diff = sizeA - sizeB

        temp1 = headA
        temp2 = headB
        if diff > 0:
            while diff > 0:
                temp1 = temp1.next
                diff -= 1
        else:
            while diff < 0:
                temp2 = temp2.next
                diff += 1
        while temp1 != temp2 :
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1
def create_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Build the shared part of the list
intersect = create_list([8, 4, 5])

# Build listA: [4, 1] + [8, 4, 5]
headA = ListNode(4, ListNode(1, intersect))

# Build listB: [5, 6, 1] + [8, 4, 5]
headB = ListNode(5, ListNode(6, ListNode(1, intersect)))

# Test
sol = Solution()
result = sol.InstersectionPointOfTwoLL(headA, headB)

if result:
    print("Intersection at node with value:", result.val)  # Output should be 8
else:
    print("No intersection")