class Node:
    def __init__(self,data=None,prev=None, next_node=None):
        self.prev = prev
        self.next = next_node
        self.data = data

class DLL:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.counter = 0
