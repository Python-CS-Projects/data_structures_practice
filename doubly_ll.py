class Node:
    def __init__(self, data=None, prev=None, next_node=None):
        self.prev = prev
        self.next = next_node
        self.data = data

    def set_prev(self, value):
        self.prev = value

    def set_next(self, value):
        self.next = value

    def get_value(self):
        print(self.data)


class Doubly_linked_list:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

# INSERT SECTION
    def insert_to_head(self, value):
        # New Node
        new_node = Node(value)
        # check if DLL is empty
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        # Add to head
        else:
            temp_node = self.head  # none <- y -> z
            self.head.set_prev(new_node)  # x <- y -> z
            self.head = new_node  # none <- x -> none
            self.head.set_next(temp_node)  # none <- x -> y
            self.count += 1

    def insert_to_tail(self, value):
        # Create a new Node with the given value
        new_node = Node(value)
        # IF DLL is empty = Head is None
        if self.count == 0:
            # Inster in the head
            self.head = new_node
            # Insert in the tail
            self.tail = new_node
            # Increase conter
            self.count += 1
        # IF head is tail (only one item in the DLL)
        if self.head is self.tail:
            # insert new NODE to head.next
            self.head.set_next(new_node)
            # Set the tail to be the New Node
            self.tail = new_node
            # add the pre of the tail
            self.tail.set_prev(self.head)
            # increase conter
            self.count += 1
        # Else
        else:
            # Set current tail.next to equal new node
            self.tail.set_next(new_node)
            # set the old tail as pre of the new tail
            new_node.set_prev(self.tail)
            # Set tail to equal new Node
            self.tail = new_node
            # increase conter
            self.count += 1


# DELETE SECTION


    def delete_head(self):
        delete_value = self.head.data
        # If count is zero
        if self.count == 0:
            # print an error
            print("Error: DLL is currently empty")
        # ELIF the head is the tail
        elif self.head is self.tail:
            # Set both to None
            self.head = None
            self.tail = None
            # Substract one from the conter or set to zero
            self.count = 0
            return delete_value
        # ELSE
        else:
            # Set the next node after the current head as the new head
            new_head = self.head.next
            self.head = new_head
            # Set the prev of the new head as None
            self.head.set_prev(None)
            # Substract one from the counter
            self.count -= 1
            return delete_value

    def delete_tail(self) -> int:
        old_tail = self.tail
        new_tail = old_tail.prev
        self.tail = new_tail
        self.tail.next = None
        return old_tail.data

    def delete_val(self, target):
        # IF empty
        if self.count == 0:
            # print an error
            print("Error: DLL is currently empty")
        # ELIF the head is the tail
        elif self.head is self.tail:
            if self.head.data is target:
                # Set both to None
                self.head = None
                self.tail = None
                # Substract one from the conter or set to zero
                self.count = 0
            else:
                print("Error: Value not found!")
        # ELSE:
        elif self.head.data is target:
            self.delete_head()
        elif self.tail.data is target:
            self.delete_tail()
        else:
            # Itenerate over the DDL
            curr_node = self.head
            while curr_node is not None:
                # IF Current value is the target
                if curr_node.data is target:
                    # Delete by setting prev next as curr val next
                    prev_node = curr_node.prev
                    next_node = curr_node.next
                    # Curr next pre as prev
                    prev_node.set_next(next_node)
                    next_node.set_prev(prev_node)
                    # Substract one from count
                    self.count -= 0

                curr_node = curr_node.next


# PRINT SECTION


    def print_val(self):
        # Current Node
        curr_node = self.head
        # Itenerate over the DLL
        while curr_node is not None:
            # Print the values
            print(curr_node.data)
            # Move the node to the next node
            curr_node = curr_node.next


# dll = Doubly_linked_list()

# dll.insert_to_head(9)
# dll.insert_to_head(3)
# dll.insert_to_tail(1)
# #dll.print_val()
# dll.delete_val(1)
# dll.print_val()
# print(dll.count)
