class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self,head):
        # Using Two pointer T.C = O(n)  and S.C = O(1)
        slow = head
        fast = head
        while fast  and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                # return True
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.val
    
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link nodes to form a cycle: 1→2→3→4→5→3...
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # cycle here

# Solution using set


# Test it
sol = Solution()
print(sol.hasCycle(node1))  # Output: True