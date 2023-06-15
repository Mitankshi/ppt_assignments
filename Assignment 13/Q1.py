class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def createNewList(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    result = None
    current1 = list1
    current2 = list2

    while current1 and current2:
        if current1.data >= current2.data:
            new_node = Node(current1.data)
            new_node.next = result
            result = new_node
        else:
            new_node = Node(current2.data)
            new_node.next = result
            result = new_node

        current1 = current1.next
        current2 = current2.next

    # Reverse the result list
    prev = None
    current = result
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    result = prev

    return result


# Create the first linked list: 5->2->3->8
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

# Create the second linked list: 1->7->4->5
list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

result = createNewList(list1, list2)

# Print the new linked list
current = result
while current:
    print(current.data, end=" ")
    current = current.next
# Output: 5->7->4->8
