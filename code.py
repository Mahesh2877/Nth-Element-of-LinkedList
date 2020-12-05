# Use this class to create linked lists.
class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)


# Implement your function below.
def nth_from_last_two_pointers(head, n):
    left = head
    right = head

    for i in range(n):
        if right is None:
            return None
        right = right.child

    while right is not None:
        left = left.child
        right = right.child
    return left


# The following function converts the given linked list into an easy-to-read string format.
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)


# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)


print("Test case 1:-")
print(linked_list_to_string(head))
print("Expected result is 1")
print(nth_from_last_two_pointers(head, 1))# should return 1.

print("Test case 2:-")
print(linked_list_to_string(head))
print("Expected result is 5")
print(nth_from_last_two_pointers(head, 5))# should return 5.

print("Test case 3:-")
print(linked_list_to_string(head2))
print("Expected result is 3")
print(nth_from_last_two_pointers(head2, 2))# should return 3.

print("Test case 4:-")
print(linked_list_to_string(head2))
print("Expected result is 1")
print(nth_from_last_two_pointers(head2, 4))# should return 1.

print("Test case 5:-")
print(linked_list_to_string(head2))
print("Expected result is None")
print(nth_from_last_two_pointers(head2, 5))# should return None.

print("Test case 6:-")
print(linked_list_to_string(None))
print("Expected result is None")
print(nth_from_last_two_pointers(None, 1))# should return None.
