class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def detectAndRemoveLoop(head):
    # Initialize pointers
    slow = fast = head

    # Find the meeting point of slow and fast pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If no loop is found, return from the function
    if fast is None or fast.next is None:
        return

    # Move the slow pointer to the head
    slow = head

    # Move both pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Set the next pointer of the node just before the loop to None
    fast.next = None

    return head


# Create the linked list: 1 -> 3 -> 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(4)

# Create the loop by connecting the last node to the node at position X=2
head.next.next.next = head.next

result = detectAndRemoveLoop(head)
print(result.data)  # Output: 1
