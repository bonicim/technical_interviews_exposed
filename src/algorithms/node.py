class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data
        return False