class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node to hold the result
    current = dummy  # Current node to build the result linked list
    carry = 0  # Carry value initialized to 0

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10  # Calculate the carry
        digit = sum % 10  # Calculate the digit

        current.next = ListNode(digit)  # Create a new node with the digit
        current = current.next  # Move the current pointer to the next node

    return (
        dummy.next
    )  # Return the result linked list starting from the next node of the dummy node


l1 = ([2, 4, 3],)
l2 = [5, 6, 4]
print(addTwoNumbers(l1=l1, l2=l2))
