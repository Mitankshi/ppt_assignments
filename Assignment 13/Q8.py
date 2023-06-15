class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


def deleteNode(head, position):
    if head is None:
        return head

    if position == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    current = head
    count = 1

    while current and count < position:
        current = current.next
        count += 1

    if not current:
        return head

    current.prev.next = current.next

    if current.next:
        current.next.prev = current.prev

    return head


# Create the doubly linked list: 1<->3<->4
head = Node(1)
head.next = Node(3)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next

position = 3

updated_list = deleteNode(head, position)
