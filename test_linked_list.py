class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class s_linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):

        tmp = self.head

        if(tmp is None):
            return

        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def insert_node(self, node):
        if(self.head is None):
            self.head = node
            return

        tmp = self.head
        while(tmp):
            if(tmp is None):
                return
            prev_node = tmp
            tmp = tmp.next

        prev_node.next = node
        node.next = None

    def reverse_list(self):
        prev_node = None
        curr_node = self.head
        while(curr_node):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def del_at_positon(self, position):
        tmp = self.head
        pos = 0
        while(pos == position-1):
            pos += 1
            prev_node = tmp
            tmp = tmp.next
        prev_node.next = tmp.next
        print(tmp.data)

    def del_node(self, key):
        tmp = self.head
        if(tmp.data == key):
            self.head = tmp.next
            return
        while(tmp):
            if(tmp.data == key):
                break
            prev_node = tmp
            tmp = tmp.next
        prev_node.next = tmp.next

    def get_size_rec(self, node):
        if(node is None):
            return 0
        return 1 + self.get_size_rec(node.next)

    def del_list(self):
        tmp = self.head
        while(tmp):
            prev_node = tmp
            del prev_node.data
            tmp = tmp.next
        self.head = None
        print("List is deleted.")

    def insert_after(self, pre_key, next_key):
        if(pre_key is None):
            return
        else:
            new_node = Node(next_key)
            new_node.next = pre_key.next
            pre_key.next = new_node


lsst = s_linked_list()
lsst.insert_node(Node('A'))
# lsst.insert_node(Node('B'))
lsst.insert_node(Node('C'))
print('size is => ', lsst.get_size_rec(lsst.head))
lsst.print_list()
print('##########')
# lsst.reverse_list()
# lsst.del_at_positon(1)
# lsst.del_node('A')
lsst.insert_after(lsst.head, 'B')
# print('##########', '\n', 'new list', '\n', '#########')
lsst.print_list()
# lsst.del_list()
# lsst.print_list()
