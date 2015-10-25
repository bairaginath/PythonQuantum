__author__ = 'bnb'

class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right



class BST():
    root=None
    def __init__(self,data):
        self.root=Node(data)

    def insert_node(self,data):
        self.__insert_node_at(self.root,data)

    def __insert_node_at(self,node,data):
        if(node==None):
            return None
        if(node.data<data):
            if node.right!=None:
                self.__insert_node_at(node.right,data)
            else:
                node.right=Node(data)
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


bst=BST(4)
bst.insert_node(2)
bst.insert_node(6)
bst.insert_node(1)
bst.insert_node(3)
bst.insert_node(5)
bst.insert_node(7)
bst.inorder_travels()

