class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def pair_wise_swap_original(self):
        temp = self.head

        # There are no nodes in ilnked list
        if temp is None:
            return

        # Traverse furthur only if there are at least two
        #  left
        while(temp is not None and temp.next is not None):

            # Swap data of node with its next node's data
            temp.data, temp.next.data = temp.next.data, temp.data

            # Move temo by 2 fro the next pair
            temp = temp.next.next

    def pair_wise_swap(self):
        cur = self.head
        if(cur is None):
            return
        # Traverse furthur only if there are at least two
        while(cur and cur.next):
            print('cur.data', cur.data)
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Driver program
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Linked list before calling pairWiseSwap() ")
llist.printList()

llist.pair_wise_swap()

print("\nLinked list after calling pairWiseSwap()")
llist.printList()
