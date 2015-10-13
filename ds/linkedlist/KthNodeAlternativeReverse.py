


class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next

class SingleLinkedList:
      head=None
      tail=None
      size=0
      def add_node(self,item):
          node=Node(item,None)
          if self.head==None:
              self.head=node
              self.tail=node
          else:
              self.tail.next=node
          self.size+=1
          self.tail=node
      def forward_travels(self):
          print("\nForward Travels")
          node=self.head
          while node!=None:
              print node.item,
              node=node.next






      def kth_node_alternative_reverse(self,k):
          if k>self.size:
             raise IndexError
          self.head=self.kth_node_alternative_reverse_recursive(self.head,k)
      def kth_node_alternative_reverse_recursive(self,node,k):
          if(node==None or node.next==None):
            return node
          first=node
          mid=node.next
          last=mid.next
          kk=k
          while(last!=None and kk>2):
             mid.next=first
             first=mid
             mid=last
             last=last.next
             kk-=1
          mid.next=first
          first=node
          first.next=self.kth_node_alternative_reverse_recursive(last, k)
          return mid






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

linkedList.forward_travels()
linkedList.kth_node_alternative_reverse(3)
linkedList.forward_travels()
linkedList.kth_node_alternative_reverse(3)
linkedList.forward_travels()



