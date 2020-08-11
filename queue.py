from doubly_ll import Doubly_linked_list
#FIFO= First in First out


class Queue:
    def __init__(self):
        self.storage = Doubly_linked_list()
        self.size = 0

    def enqueue (self,value):#Push to the tail of the line
        self.size += 1
        self.storage.insert_to_tail(value)
        
    def dequeue(self):  # pop the first item at the head
        if self.size > 0:
            self.size -= 1
            return self.storage.delete_head()   

    def get_len(self):
        return f"Current size: {self.size}"

    def get_values(self):
        self.storage.print_val()

queue = Queue()

queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# x = queue.dequeue()
# print(x)
# queue.get_values()
# print(queue.get_len())
