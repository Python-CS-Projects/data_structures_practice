from doubly_ll import Doubly_linked_list

class Queue:#FIFO
    def __init__(self):
        self.storage = Doubly_linked_list()
        self.size = 0

    def push(self,value):#Push to the tail of the line
        self.size += 1
        self.storage.insert_to_tail(value)
        

    def pop(self):#pop the first item at the head
        if self.size > 0:
            self.size -= 1
        self.storage.delete_head()   

    def get_len(self):
        return f"Current size: {self.size}"

    def get_values(self):
        self.storage.print_val()

# queue = Queue()

# queue.push(4)
# queue.push(5)
# queue.push(6)
# queue.pop()

# queue.get_values()
# print(queue.get_len())
