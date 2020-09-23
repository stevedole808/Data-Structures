"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value:int = value
        self.left: BinarySearchTree = None
        self.right: BinarySearchTree = None

    # Insert the given value into the tree
    def insert(self, insert_value: int):
        if self.value is None:
            self.value = insert_value
        else:
            if insert_value >= self.value:
                if self.right is None:
                    self.right = BinarySearchTree(insert_value)
                else:
                    self.right.insert(insert_value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(insert_value)
                else:
                    self.left.insert(insert_value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target: int):
        # when we start searching self will be the value 
        # compare the target against self(node)

        # Criteria for returning False: we know we need to go in one direction, but there's nothing in the left  or right direction
        # if target == self value
            # Return true
        # if target is less then selfs value we need to go left
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is BSTNode
            if not self.right:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        current = self.value
        if self.right is not None:
            current = self.right
        else:
            return current

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

