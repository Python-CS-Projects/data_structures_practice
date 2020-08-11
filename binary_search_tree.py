# Is like a linked list but each node points to no more than two nodes
# Root is the topmost node
# Left is less or equal than the parent
# Right is bigger than the parent
class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        #Create a new_node
        new_node = BinarySearchTree(new_value)
        #Check IF new_value > self.value then go right
        if new_value > self.value:
            #IF right is None
            if self.right is None:
                #Set the right to the New Value
                self.right = new_node
            #ELSE
            else:
                #Recurse on the rigth
                self.right.insert(new_value)
        
        #ELIF new_value < self.value then go left
        elif new_value < self.value:
            #IF LEFT is NONE
            if self.left is None:
                #SET the left to the new node
                self.left = new_node
            #ELSE
            else:
                #Recursive case
                self.left.insert(new_value)


bst = BinarySearchTree(20)
bst.insert(3)
bst.insert(3)
bst.insert(3)
