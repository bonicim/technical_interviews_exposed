class Node:
    # data must be an integer
    # **kwargs should only pass the following keyword arguments: 
    # parent=Node(), left=Node(), right=Node()
    def __init__(self, data, **kwargs):
            self.data = data
            self.parent = None
            self.left = None
            self.right = None
                        
            if kwargs is not None:
                for key, val in kwargs.items():
                    setattr(self, key, val)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data
        return False