class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverseKNodes(head, k):
    if head is None or k == 1:
        return head

    def reverseList(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def getKthNode(node, k):
        count = 1
        while count < k and node:
            node = node.next
            count += 1
        return node

    dummy = Node(0)
    dummy.next = head
    current = dummy

    while current:
        kth_node = getKthNode(current, k)
        if kth_node is None:
            break

        next_node = kth_node.next
        kth_node.next = None

        current.next = reverseList(current.next)

        while current.next:
            current = current.next

        current.next = next_node
        current = next_node

    return dummy.next


# Create the linked list: 1->2->2->4->5->6->7->8
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

k = 4

result = reverseKNodes(head, k)
