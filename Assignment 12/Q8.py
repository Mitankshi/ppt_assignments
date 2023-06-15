class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def isCircular(head):
    if head is None:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create a circular linked list: 1->2->3->4->5->6->7->8->(back to 1)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# ... Continue creating the rest of the nodes

# Make the last node connect back to the first node, creating a cycle
current = head
while current.next:
    current = current.next
current.next = head

result = isCircular(head)
print(result)  # Output: True
