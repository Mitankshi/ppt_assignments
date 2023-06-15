class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


# Create the linked list: 11->11->11->21->43->43->60
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

result = removeDuplicates(head)

# Print the modified linked list
current = result
while current:
    print(current.data, end=" ")
    current = current.next
# Output: 11->21->43->60
