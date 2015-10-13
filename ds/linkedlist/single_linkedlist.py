


class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next

class SingleLinkedList:
      head=None
      tail=None
      def add_node(self,item):
          node=Node(item,None)
          if self.head==None:
              self.head=node
              self.tail=node
          else:
              self.tail.next=node
          self.tail=node
      def forward_travels(self):
          print("Forward Travels")
          node=self.head
          while node!=None:
              print node.item
              node=node.next

      def remove(self, node_value):
          current_node = self.head
          previous_node = None
          while current_node is not None:
              if current_node.item == node_value:
                 # if this is the first node (head)
                 if previous_node is not None:
                    previous_node.next = current_node.next
                 else:
                    self.head = current_node.next

              # needed for the next iteration
              previous_node = current_node
              current_node = current_node.next


linkedList=SingleLinkedList()
linkedList.add_node(1)
linkedList.add_node(2)
linkedList.add_node(3)
linkedList.add_node(4)
linkedList.add_node(5)

linkedList.forward_travels()
linkedList.remove(3)
linkedList.forward_travels()


