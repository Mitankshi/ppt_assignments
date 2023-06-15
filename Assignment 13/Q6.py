class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    dummy = Node()  # Dummy node to hold the merged list
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return dummy.next


# Create the first linked list: 5->10->15
a = Node(5)
a.next = Node(10)
a.next.next = Node(15)

# Create the second linked list: 2->3->20
b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

merged_list = mergeLists(a, b)
