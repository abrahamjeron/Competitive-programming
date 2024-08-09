class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_position(head, data, k):
    new_node = Node(data)
    
    if k == 0:  # Insert at the head
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    current = head
    for _ in range(k - 1):
        if current is None:
            print("Position out of bounds.")
            return head
        current = current.next

    if current is None:
        print("Position out of bounds.")
        return head

    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current

    return head

def print_ll(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Example usage
elements = [1, 2, 3, 4]
head = Node(elements[0])
current = head

for element in elements[1:]:
    new_node = Node(element)
    current.next = new_node
    new_node.prev = current
    current = new_node

print("Original list:")
print_ll(head)

data_to_insert = 5
position = 2
print(f"Inserting {data_to_insert} at position {position}:")
head = insert_at_position(head, data_to_insert, position)

print("Updated list:")
print_ll(head)
