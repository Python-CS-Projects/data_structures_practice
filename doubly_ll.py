class Node:
    def __init__(self, data=None, prev=None, next_node=None):
        self.prev = prev
        self.next = next_node
        self.data = data


class DLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

# INSERT SECTION
    def insert_to_head(self, value):
        #New Node
        new_node = Node(value)
        #check if DLL is empty
        if self.count is 0:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        #Add to head
        else:
            temp_node = self.head # none <- y -> z
            self.head.prev = new_node  # x <- y -> z
            self.head = new_node  # none <- x -> none
            self.head.next = temp_node  # none <- x -> y
            self.count += 1


    def insert_to_tail(self, value):
        pass

# DELETE SECTION
    def delete_head(self):
        pass

    def delete_tail(self):
        pass

    def delete_val(self, value):
        pass

# PRINT SECTION
    def print_val(self):
        #Current Node
        curr_node = self.head
        #Itenerate over the DLL
        while curr_node is not None:
            #Print the values
            print(curr_node.data)
            #Move the node to the next node 
            curr_node = curr_node.next


dll = DLL()

dll.insert_to_head(9)
dll.insert_to_head(3)
dll.print_val()
