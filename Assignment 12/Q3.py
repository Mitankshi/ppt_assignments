class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def findNthNodeFromEnd(head, N):
    slow = fast = head

    # Move the "fast" pointer N nodes ahead
    for _ in range(N):
        if fast is None:
            # N is greater than the number of nodes
            return None
        fast = fast.next

    # Move both pointers simultaneously until the "fast" pointer reaches the end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # At this point, "slow" is pointing to the Nth node from the end
    return slow.data


# Create the linked list: 1->2->3->4->5->6->7->8->9
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# ... Continue creating the rest of the nodes

N = 2
result = findNthNodeFromEnd(head, N)
print(result)  # Output: 8
