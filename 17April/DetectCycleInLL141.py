class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self,head):
        # T.C = O(n) and S.C = O(n)
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False

        # Using Two pointer T.C = O(n)  and S.C = O(1)
        slow = head
        fast = head
        while fast  and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        return False
    
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
class Solution:
    def hasCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False

# Test it
sol = Solution()
print(sol.hasCycle(node1))  # Output: True