class Node:
    # This is an everything Node. It can be used to create a graph, linkedlist, binary tree, circular linkedlist
    # data must be an integer
    # **kwargs should only pass the following keyword arguments:
    # parent=Node(), tail=Node(), left=Node(), right=Node(), left=Node(), right=Node(), neighbors=[Node()]
    def __init__(self, data, **kwargs):
        self.data = data
        self.parent = None
        self.tail = None
        self.left = None
        self.right = None
        self.next = None
        self.neighors = None

        if kwargs is not None:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data
        return False
