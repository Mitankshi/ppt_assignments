class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def retainDelete(head, M, N):
    current = head
    prev = None

    while current:
        # Move current M steps ahead
        for _ in range(M):
            if current is None:
                return head
            prev = current
            current = current.next

        # Move prev N steps ahead
        for _ in range(N):
            if prev is None:
                return head
            prev = prev.next

        # Delete the next N nodes
        prev.next = current

    return head


# Create the linked list: 1->2->3->4->5->6->7->8
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# ... Continue creating the rest of the nodes

M = 2
N = 2

result = retainDelete(head, M, N)

# Print the modified linked list
current = result
while current:
    print(current.data, end=" ")
    current = current.next
# Output: 1->2->5->6
