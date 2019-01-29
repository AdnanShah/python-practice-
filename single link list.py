class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class s_link_list:
    def __init__(self):
        self.head = None

    def insert_at(self, pre_node, next_node):
        if(pre_node is None):
            print("Error")
        else:
            new_node = Node(next_node)
            new_node.next = pre_node.next
            pre_node.next = new_node

    def preappend_node(self, node):
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node

    def append_node(self, node):
        new_node = Node(node)
        if(self.head is None):
            self.head = new_node
        else:
            last_node = self.head
            while(last_node.next):
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        last_node = self.head
        cunt = 0
        while(last_node):
            print("position", cunt, last_node.data)
            cunt += 1
            last_node = last_node.next

    def del_link_list(self):
        tmp = self.head
        while(tmp):
            prev_node = tmp
            del tmp.data
            tmp = tmp.next

    def detect_loop(self):
        tmp = self.head
        s = set()
        while(tmp):
            if(tmp in s):
                return True
            s.add(tmp)
            tmp = tmp.next

        return False

    def detect_loop_2(self):
        slow_tmp = self.head
        fast_tmp = self.head
        while(slow_tmp and fast_tmp and fast_tmp.next):
            slow_tmp = slow_tmp.next
            fast_tmp = fast_tmp.next.next
            print("detect_loop_2 => ", slow_tmp.data,
                  fast_tmp.data, fast_tmp.next.data)

            if(slow_tmp == fast_tmp):
                print('Loop detected')
                return

    def get_size(self):
        tmp = self.head
        # iterative way
        count = 0
        while(tmp):
            count += 1
            tmp = tmp.next
        print('Length', count)

    def deleteNode(self, key):
        tmp = self.head
        if(tmp is not None):
            if(tmp.data == key):
                self.head = tmp.next
                tmp = None
                return

        while(tmp is not None):
            if(tmp.data == key):
                print("key =>", tmp.data, '\n\n')
                break
            prev_node = tmp
            tmp = tmp.next

        if(tmp == None):
            return
        prev_node.next = tmp.next
        tmp = None

    def del_node_at_position(self, position):
        tmp = self.head
        if(tmp is None):
            return

        if(position == 0):
            self.head = tmp.next
            tmp = None
            return
        pos = 0
        while(pos < position-1):
            pos += 1
            tmp = tmp.next
            if(tmp is None):
                break

        if(tmp is None):
            print("tmp is None")
            return
        if(tmp.next is None):
            print('tmp.next is None')
            return

        prev_node = tmp
        next_node = tmp.next.next
        tmp.next = None
        prev_node.next = next_node

    def get_size_rec(self, node):
        if(node is None):
            return 0
        return 1 + self.get_size_rec(node.next)

    def swap_node(self, key_1, key_2):
        if(key_1 == key_2):
            return

        prev_1 = None
        curr_1 = self.head
        while(curr_1 and curr_1.data is not key_1):
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while(curr_2 and curr_2.data is not key_2):
            prev_2 = curr_2
            curr_2 = curr_2.next
        if(curr_1 is None or curr_2 is None):
            print("key not found.....")
            return

        if(prev_1 is not None):
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if(prev_2 is not None):
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse(self):
        prev_node = None
        tmp = self.head
        while(tmp):
            next_node = tmp.next
            tmp.next = prev_node
            prev_node = tmp
            tmp = next_node
        self.head = prev_node

    def swap_node_2(self, key_1, key_2):
        if(key_1 == key_2):
            return

        prev_1 = None
        curr_1 = self.head
        while(curr_1 and curr_1.data != key_1):
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while(curr_2 and curr_2.data != key_2):
            prev_2 = curr_2
            curr_2 = curr_2.next

        if(curr_1 is None or curr_2 is None):
            print("key not found.")
            return
        else:
            print(curr_1.data, curr_2.data)

        if(prev_1 is not None):
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if(prev_2 is not None):
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_2.next, curr_1.next = curr_1.next, curr_2.next

    def nth_node(self, node_number):
        tmp = self.head
        list_length = 0
        while(tmp):
            if(list_length == node_number):
                break
            list_length += 1
            tmp = tmp.next
        print(tmp.data)

    def middle_element_2(self):
        lst = []
        tmp = self.head
        while(tmp):
            lst.append(tmp)
            tmp = tmp.next
        # print(len(lst)/2)
        print(lst[len(lst)//2].data)

    def middle_element_3(self):
        tmp = self.head
        mid = self.head
        cunt = 0
        while(tmp):
            if(cunt & 1):
                mid = mid.next
            cunt += 1
            tmp = tmp.next
        print(mid.data)

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if(slow_p == fast_p):
                print('loop detected => ', slow_p.data)
                return

    def loop_hash_detech(self):
        tmp = self.head
        hash_look_up = set()
        while(tmp):

            if(tmp in hash_look_up):
                return True
            hash_look_up.add(tmp)
            tmp = tmp.next
        return False

    def remove_dup(self):
        s = set()
        prev = None
        cur = self.head
        while(cur):
            if(cur.data in s):
                # remove node
                prev.next = cur.next
                cur = None
            else:
                # move on
                s.add(cur.data)
                prev = cur
            cur = prev.next

    def merge_list(self, llist):
        cur_1 = self.head
        cur_2 = llist.head
        prev_node = None
        if(not cur_1):
            return cur_2
        if(not cur_2):
            return cur_1
        if(cur_1 and cur_2):
            if(cur_1.data <= cur_2.data):
                prev_node = cur_1
                cur_1 = prev_node.next
            else:
                prev_node = cur_2
                cur_2 = prev_node.next
        new_head = prev_node
        while(cur_1 and cur_2):
            if(cur_1.data <= cur_2.data):
                prev_node.next = cur_1
                prev_node = cur_1
                cur_1 = prev_node.next
            else:
                prev_node.next = cur_2
                prev_node = cur_2
                cur_2 = prev_node.next
        if(not cur_1):
            prev_node.next = cur_2
        if(not cur_2):
            prev_node.next = cur_1
        return new_head

    def nth_to_last(self, node_number):
        cur_node = self.head
        count = 1
        while(cur_node and count != node_number):
            count += 1
            cur_node = cur_node.next
        self.head = cur_node

    def move_tail_to_head(self):
        prev_node = None
        last_node = self.head

        while(last_node.next):
            prev_node = last_node
            last_node = last_node.next

        prev_node.next = None
        last_node.next = self.head
        self.head = last_node

    def nth_from_last(self, n):
        length = 0
        tmp = self.head
        while(tmp):
            tmp = tmp.next
            length += 1
        tmp = self.head

        for i in range(length - n):
            tmp = tmp.next
        print('temp.data = >', tmp.data)

    def is_palindrom_new(self):

        length = 0
        tmp = self.head
        prev = []
        while(tmp):
            prev.append(tmp)
            length += 1
            tmp.next
        return length
        # mid = 0
        # tmp = self.head
        # print('asdads')
        # while(mid <= length//2):
        #     if(prev[-length] != tmp.data):
        #         return False
        #     tmp = tmp.next
        #     mid += 1
        # print('asdad')
        # return True


lsst_1 = s_link_list()
lsst_1.append_node(1)
lsst_1.append_node(3)
lsst_1.append_node(5)
lsst_1.append_node(7)
lsst_1.append_node(9)

print('\nlist 1 :##########\n')
lsst_1.print_list()
print('is_palindrom => ', lsst_1.is_palindrom_new())


# lsst_1.head.next.next.next.next.next = lsst_1.head
# lsst_1.detect_loop_2()
# lsst_1.print_list()


# print('list nth_from_last:##########\n')
# lsst_1.nth_from_last(4)
# lsst_1.print_list()

# print('list move_tail_to_head :##########\n')
# lsst_1.move_tail_to_head()
# lsst_1.print_list()

# print('list nth_to_last :##########\n')
# lsst_1.nth_to_last(3)
# lsst_1.print_list()


# lsst_2 = s_link_list()
# lsst_2.append_node(2)
# lsst_2.append_node(4)
# lsst_2.append_node(6)

# print('list 1 :##########\n')
# lsst_1.print_list()
# print('list 2: ##########\n')
# lsst_2.print_list()
# print('Merge List: ########## \n')
# lsst_1.merge_list(lsst_2)
# lsst_1.print_list()

# lsst_1.head.next.next = lsst_1.head
# lsst_1.remove_dup()
# lsst_1.print_list()
# lsst_1.middle_element_2()
# lsst_1.middle_element_3()
# lsst_1.detectLoop()
# print(lsst_1.loop_hash_detech())
# lsst_1.print_list()
# lsst_1.nth_node(2)
# lsst_1.swap_node_2('B', 'D')
# print('##########')
# lsst_1.print_list()
# lsst_1.reverse()
# print(lsst_1.get_size_rec(lsst_1.head))
# lsst_1.del_node_at_position(1)
# lsst_1.get_size()
# lsst_1.detect_loop_2()
# lsst_1.preappend_node('B')
# lsst_1.deleteNode('C')
# lsst_1.insert_at(lsst_1.head.next, 'C')
# lsst_1.del_link_list()

# if(lsst_1.detect_loop()):
#     print("Loop detected")
# else:
#     print("Loop not detected")
