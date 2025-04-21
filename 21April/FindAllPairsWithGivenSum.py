class ListNode:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def findAllPairsWithSum(self,head,target):
        # Using Brute Force
        result = []
        # temp = head
        # while temp:
        #     new_node = temp.next
        #     second_sum = target - temp.val
        #     while new_node:
        #         if new_node.val == second_sum:
        #             result.append((temp.val,new_node.val))
        #         new_node = new_node.next
        #     temp = temp.next
        # return result

        # Using Two Pointers
        tail = head
        while tail:
            tail = tail.next
        start = head
        end = tail
        while start != end and start.prev != end:
            curr_sum = start.val + end.val
            if curr_sum == target:
                result.append((start.val,end.val))
                start = start.next
                end = end.prev
            elif curr_sum < target:
                start = start.next
            else:
                end = end.prev
        return result
# Creating a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(9)

n1.next = n2
n2.prev, n2.next = n1, n3
n3.prev, n3.next = n2, n4
n4.prev, n4.next = n3, n5
n5.prev = n4

sol = Solution()
print(sol.findAllPairsWithSum(n1, 5))  # Output: [(1, 5), (2, 4)]

