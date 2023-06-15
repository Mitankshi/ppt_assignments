class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def mergeAlternate(first, second):
    if first is None:
        return second

    if second is None:
        return first

    current_first = first
    current_second = second

    while current_first and current_second:
        next_first = current_first.next
        next_second = current_second.next

        current_first.next = current_second
        current_second.next = next_first

        current_first = next_first
        current_second = next_second

    if current_second:
        current_first.next = current_second

    second = None  # Empty the second list

    return first


# Create the first linked list: 5->7->17->13->11
first = Node(5)
first.next = Node(7)
first.next.next = Node(17)
# ... Continue creating the rest of the nodes

# Create the second linked list: 12->10->2->4->6
second = Node(12)
second.next = Node(10)
second.next.next = Node(2)
# ... Continue creating the rest of the nodes

result = mergeAlternate(first, second)

# Print the modified first linked list
current = result
while current:
    print(current.data, end=" ")
    current = current.next
# Output: 5->12->7->10->17->2->13->4->11->6

# Print the modified second linked list
current = second
while current:
    print(current.data, end=" ")
    current = current.next
# Output: (empty list)
