class Node:
    def __init__(self, data=None, prev=None, next_node=None):
        self.prev = prev
        self.next = next_node
        self.data = data

    def insert_prev(self,value):
        self.prev = value

    def insert_next(self,value):
        self.next = value

    def get_value(self):
        print(self.data)
        

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
        #Create a new Node with the given value
        new_node = Node(value)
        #IF DLL is empty = Head is None
        if self.count is 0:
            #Inster in the head 
            self.head = new_node
            #Insert in the tail
            self.tail = new_node
        #IF head is tail (only one item in the DLL)
        if self.head is self.tail:
            #insert new NODE to head.next
            self.head.next = new_node
            #Set the tail to be the New Node
            self.tail = new_node
        #Else 
        else:
            #Set current tail.next to equal new node
            self.tail.next = new_node
            #Set tail to equal new Node
            self.tail = new_node
            

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
dll.insert_to_tail(1)
dll.insert_to_tail(2)
dll.insert_to_tail(3)
dll.print_val()
