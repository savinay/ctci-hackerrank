""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys
max_val = sys.maxint
min_val = -sys.maxint - 1
def check_binary_search_tree_helper(root, min_value, max_value):
    if root is None:
        return True
    if root.data < min_value or root.data > max_value:
        return False
    return (check_binary_search_tree_helper(root.left, min_value, root.data-1) and check_binary_search_tree_helper(root.right, root.data+1, max_value))
    

def check_binary_search_tree_(root):
    return check_binary_search_tree_helper(root, min_val, max_val)
  

#Alternative solution

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
arr = []
def in_order(root):
    if root:
        in_order(root.left)
        arr.append(root.data)
        in_order(root.right)

def check_binary_search_tree_(root):
    in_order(root)
    for i in xrange(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True
  
