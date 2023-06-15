class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def deleteLastOccurrence(head, key):
    if head is None:
        return None

    last_occurrence = None
    prev_last_occurrence = None
    current = head
    prev = None

    while current:
        if current.data == key:
            last_occurrence = current
            prev_last_occurrence = prev
        prev = current
        current = current.next

    if last_occurrence:
        if prev_last_occurrence:
            prev_last_occurrence.next = last_occurrence.next
        else:
            head = head.next

    return head


# Create the linked list: 1->2->3->5->2->10
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(10)

key = 2

result = deleteLastOccurrence(head, key)
