

__author__ = 'bnb'

class Node():
    def __init__(self,data,left=None,right=None,leftFlag=0,rightFlag=0):
        self.data=data
        self.left=left
        self.right=right
        self.leftFlag=leftFlag
        self.rightFlag=rightFlag



class InorderThreadedBST():
    root=None
    def __init__(self,data):
        self.root=Node(data)

    def insert_node(self,data):
        self.__insert_node_at(self.root,data)

    def __insert_node_at(self,node,data):
        if(node==None):
            return None
        if(node.data<data):
            if node.rightFlag==1:
                node.right=Node(data,right=node.right,rightFlag=1)
            if node.right==None and node.rightFlag==0:
                node.right=Node(data,left=node,leftFlag=1)
            else:
                self.__insert_node_at(node.right,data)
        else:
            if node.left!=None:
                self.__insert_node_at(node.left,data)
            else:
                node.left=Node(data)
    def inorder_travels(self):
        self.__inorder_travels_at(self.root)
    def __inorder_travels_at(self,node):
        if node==None:
            return
        self.__inorder_travels_at(node.left)
        print node.data ,
        self.__inorder_travels_at(node.right)


bst=InorderThreadedBST(4)
bst.insert_node(2)
bst.insert_node(6)
bst.insert_node(1)
bst.insert_node(3)
bst.insert_node(5)
bst.insert_node(7)
bst.inorder_travels()


