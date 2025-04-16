class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
def FindMiddleOfLL(head):
    #using Brute Force

    # count =0 
    # temp = head
    # while temp:
    #     count  += 1
    #     temp = temp.next
    # temp = head
    # count1 = 0
    # while temp:
    #     if count1 == count // 2 :
    #         return temp 
    #     count1 += 1
    #     temp = temp.next

    # # Now go to the middle node
    # mid = count // 2
    # temp = head
    # for _ in range(mid):
    #     temp = temp.next
    # return temp

    # Using Two pointer
    slow = head
    fast = head
    while fast  and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

       


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_from_middle(head):
    mid = FindMiddleOfLL(head)
    while mid:
        print(mid.val, end=" ")
        mid = mid.next
    print() 


head = create_linked_list([1, 2, 3, 4, 5,7,9])
print_from_middle(head)  


head = create_linked_list([1, 2, 3, 4, 5, 6])
print_from_middle(head)  