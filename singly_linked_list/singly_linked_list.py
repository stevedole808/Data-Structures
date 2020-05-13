class Node:
    def __init__(self, value = None, next_node = None):
        # value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.new_next = new_next

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the list
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
    
    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # What if the list is empty?
        if not self.head and not self.tail:
            # set both to the new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            self.value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()

    def contains(self):
        current = self.head
        while current is not None:
            print(current.value)

ll = LinkedList()

    



        