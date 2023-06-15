class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def isPalindrome(head):
    # Store characters in a list or stack
    characters = []
    current = head
    while current:
        characters.append(current.data)
        current = current.next

    # Initialize pointers
    start = 0
    end = len(characters) - 1

    # Compare characters at corresponding positions
    while start < end:
        if characters[start] != characters[end]:
            return False
        start += 1
        end -= 1

    return True


# Create the linked list: R->A->D->A->R->NULL
head = Node("R")
head.next = Node("A")
head.next.next = Node("D")
# ... Continue creating the rest of the nodes

result = isPalindrome(head)
print(result)  # Output: True

# Create the linked list: C->O->D->E->NULL
head = Node("C")
head.next = Node("O")
head.next.next = Node("D")
# ... Continue creating the rest of the nodes

result = isPalindrome(head)
print(result)  # Output: False
