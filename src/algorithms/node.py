class Node:
    def __init__(self, mydata):
        self.left = None
        self.right = None
        self.data = mydata

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data
        return False