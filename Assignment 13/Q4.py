class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverseAlternateKNodes(head, k):
    if head is None or k == 1:
        return head

    def reverseList(node, k):
        prev = None
        current = node
        count = 0
        while count < k and current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        if node:
            node.next = current
        count = 0
        while count < k - 1 and current:
            current = current.next
            count += 1
        if current:
            current.next = reverseList(current.next, k)
        return prev

    return reverseList(head, k)


# Create the linked list: 1->2->3->4->5->6->7->8->9
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

k = 3

result = reverseAlternateKNodes(head, k)
