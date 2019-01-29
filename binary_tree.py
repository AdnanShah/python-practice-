class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def pre_order_traverse(self, new_node, new_string):
        if(new_node):
            new_string += (str(new_node.value) + ' => ')
            new_string = self.pre_order_traverse(new_node.left, new_string)
            new_string = self.pre_order_traverse(new_node.right, new_string)
        return new_string

    def in_order_traverse(self, new_node, out_string):
        if(new_node):
            out_string += (str(new_node.value) + ' => ')
            out_string = self.in_order_traverse(new_node.left, out_string)
            out_string = self.in_order_traverse(new_node.right, out_string)
        return out_string

    def post_order_traverse(self, new_node, out_string):
        if(new_node is None):
            out_string += '-1'
            return out_string
        else:
            out_string = self.in_order_traverse(new_node.left, out_string)
            out_string = self.in_order_traverse(new_node.right, out_string)
            out_string += (str(new_node.value) + ' => ')
        return out_string


tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# print("\npre_order_traverse\n", tree.pre_order_traverse(tree.root, ''))
# print("\nin_order_traverse\n", tree.in_order_traverse(tree.root, ""))
print("\npost_order_traverse\n", tree.post_order_traverse(tree.root, ""))
