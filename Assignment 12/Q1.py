class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddleNode(head):
    if head is None or head.next is None:
        return None

    dummy = ListNode(0)  # Create a dummy node to handle the case of deleting the head
    dummy.next = head
    slow = dummy
    fast = dummy
    prev = dummy

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next  # Delete the middle node

    return dummy.next


head = "1 -> 2 -> 4 -> 5"
deleteMiddleNode(head=head)
