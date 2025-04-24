class ListNode:
    def __init__(self,val = None,next=None):
        self.val = val
        self.next = next
class Solution:
    def ReomeNthNodeFromEndOFSL(self,head,n):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        steps = count - n
        if steps == 0:
            return head.next
        temp = head
        for _ in range(steps - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
# Create a list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
new_head = sol.ReomeNthNodeFromEndOFSL(head, 2)

# Print the modified list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output: 1 -> 2 -> 3 -> 5 ->
