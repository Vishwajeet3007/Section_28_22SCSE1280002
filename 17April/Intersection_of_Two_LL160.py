class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class Solution:

    def sizeOfLL(self,head):
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def getIntersectionNode(self,headA,headB):
        sizeA = self.sizeOfLL(headA)
        sizeB = self.sizeOfLL(headB)
        diff = sizeA - sizeB

        ptr1 = headA
        ptr2 = headB
        if diff > 0:
            while diff > 0:
                ptr1 = ptr1.next
                diff -=1
        elif diff < 0:
            while diff < 0:
                ptr2 = ptr2.next
                diff +=1
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1



# Creating nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node8 = ListNode(8)
node9 = ListNode(9)

# Creating List A: 1 → 2 → 3 → 8 → 9
node1.next = node2
node2.next = node3
node3.next = node8
node8.next = node9

# Creating List B: 4 → 8 → 9
node4.next = node8  # Intersection happens at node8

# Finding intersection
sol = Solution()
intersection_node = sol.getIntersectionNode(node1, node4)

# Output the intersection node value
if intersection_node:
    print(f"Intersection at node with value: {intersection_node.val}")
else:
    print("No intersection")


        