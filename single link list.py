class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class s_linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self, data):

        if(self.head is None):
            self.head = data
        else:
            curr_node = self.head
            while True:
                if (curr_node.next is None):
                    break
                curr_node = curr_node.next
            curr_node.next = data

    def print_lst(self):
        current_node = self.head
        while True:
            if(current_node is None):
                break
            print(current_node.data)
            current_node = current_node.next


linkedlist = s_linked_list()
node_1 = Node('Node_1')
node_2 = Node('Node_2')
linkedlist.insert_node(node_1)
linkedlist.insert_node(node_2)
linkedlist.print_lst()
