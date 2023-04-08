# Linked List

# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    # L is at head
    # R is two steps ahead
    # Once right reaches end, we know left is at the n from the end
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
            
    left.next = left.next.next
        
    return dummy.next