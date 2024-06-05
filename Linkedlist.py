class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Example usage:
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Append elements
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Print the linked list
    print("Linked List:")
    linked_list.print_list()

    # Search for an element
    print("\nSearch for 2:", linked_list.search(2))

    # Delete an element
    linked_list.delete(2)

    # Print the linked list after deletion
    print("\nLinked List after deletion:")
    linked_list.print_list()