class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node

    head = prev
    head.prev = None

    return head


# Create the doubly linked list: 10<->8<->4<->2
head = Node(10)
head.next = Node(8)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next

reversed_list = reverseLinkedList(head)
