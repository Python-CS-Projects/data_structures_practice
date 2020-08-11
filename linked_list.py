class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert to tail

    def reverse_ll(self):
        #Current node
        curr_node = self.head
        #Prev pointer
        prev = None
        #Loop over the LL
        while curr_node is not None:
            #Flip the values
            next_node = curr_node.next_node # 1 > 2 > 3 -- next = 2 -- next = 3 -- next = None
            curr_node.next_node = prev # 1 > None -- 2 > 1 > None -- 3 > 2 > 1 > None
            prev = curr_node # prev = 1 -> None -- prev = 2 -- prev = 3

            #Move curr pointer to next to keep loop
            curr_node = next_node
        #after loop completes set the last prev to be the head = 3
        self.head = prev

    def insert_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node #Setting the tail as the head for a ll with one item makes it easier to handle logic
        else:
            current_val = self.head
            while current_val.next_node != None:
                current_val = current_val.next_node
            current_val.next_node = node#add the new node to the tail
            self.tail = node# set the new node as the tail optional

    # Insert to head
    def insert_to_head(self, value):
        node = Node(value)
        if self.head is None:#if the ll is empty
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head#set the next node of the new head
            self.head = node #set as head
    # delete from tail
    def delete_tail(self):
        if self.head is None:
            print("Error the linked list is empty")
            return
        elif self.head is self.tail:#only one item in the list
            self.head = None
        else:
            current_value = self.head
            while current_value is not None:
                if current_value.next_node is self.tail:
                    current_value.next_node = None
                    self.tail = current_value
                    return
                current_value = current_value.next_node
            

    # delete from head
    def delete_head(self):
        if self.head is None:#empoty ll
            print("Error the linked list is empty")
            return
        elif self.head is self.tail: #if there is only one item
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next_node
            self.head = new_head


    def print_values(self):
        curr_val = self.head
        print("---------")
        while curr_val != None:
            print(curr_val.value)
            curr_val = curr_val.next_node
        print("---------")


linked_list = LinkedList()

linked_list.insert_to_head(4)
linked_list.insert_to_tail(5)
linked_list.insert_to_tail(10)
linked_list.print_values()
# linked_list.delete_tail()
# linked_list.delete_head()
linked_list.reverse_ll()
linked_list.print_values()
