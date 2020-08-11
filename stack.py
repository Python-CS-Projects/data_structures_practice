from doubly_ll import Doubly_linked_list


class Stack:  # Fist in last out
    def __init__(self):
        self.storage = Doubly_linked_list()
        self.count = 0

    def push(self, value):
        self.storage.insert_to_tail(value)
        self.count += 1

    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.storage.delete_tail()
        else:
            print("Error: Cannot delete from an empty stack.")
            return

    def get_len(self):
        return self.count

    def get_values(self):
        if self.count > 0:
            self.storage.print_val()
        else:
            print("Empty Stack")

stack = Stack()

# stack.push(4)
# stack.push(20)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.get_values()
