


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

      def reverse(self):
          first=self.head
          mid=first.next
          last=mid.next
          first.next=None
          self.tail=first
          while(last!=None):
              mid.next=first
              first=mid
              mid=last
              last=last.next
          mid.next=first
          self.head=mid

      def alternative_reverse_linkedlist(self):
          first=self.head
          mid=first.next
          self.head=mid
          last=mid.next
          while(last!=None and last.next!=None):
              mid.next=first
              first.next=last.next
              first=last
              mid=first.next
              last=mid.next
          first.next=last
          mid.next=first








linkedList=SingleLinkedList()
linkedList.add_node(1)
linkedList.add_node(2)
linkedList.add_node(3)
linkedList.add_node(4)
linkedList.add_node(5)
linkedList.add_node(6)
linkedList.add_node(7)
linkedList.add_node(8)
linkedList.add_node(9)
linkedList.add_node(10)
linkedList.add_node(11)

linkedList.alternative_reverse_linkedlist()
linkedList.forward_travels()

linkedList.forward_travels()
