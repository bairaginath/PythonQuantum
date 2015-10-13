class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLInkedList(object):

    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def forward_travels(self):
        print("Forward Travels")
        node=self.head
        while(node!=None):
            print node.data
            node=node.next

    def backward_travels(self):
        print("Backward Travels")
        node=self.tail
        while(node!=None):
            print node.data
            node=node.prev


d = DoubleLInkedList()

d.append(5)
d.append(6)
d.append(50)
d.append(30)
d.append(70)
d.append(60)


d.forward_travels()
d.backward_travels()

d.remove(50)
d.forward_travels()
d.backward_travels()


