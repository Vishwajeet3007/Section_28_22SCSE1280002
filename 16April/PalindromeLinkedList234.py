class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):

        self.current=None
    def recursion(self,head):
        if head==None:
            return True
        output=self.recursion(head.next)
        if not output:
            return False
        if head.val != self.current.val:
            return False
        self.current=self.current.next
        return output
    def isPalindrome(self, head):
        self.current=head
        return self.recursion(head)
    
def build_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Test cases
sol = Solution()
head1 = build_linked_list([1, 2, 2, 1])
print(sol.isPalindrome(head1))  # Output: True

sol = Solution()
head2 = build_linked_list([1, 2])
print(sol.isPalindrome(head2))  # Output: False