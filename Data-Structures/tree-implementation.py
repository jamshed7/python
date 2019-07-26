class BinaryTree(object):
    def __init__(self,new_root):
        self.key = new_root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,new_child):
        if self.leftChild == None:
            self.leftChild = BinaryTree(new_child)
        else:
            t = BinaryTree(new_child)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,new_child):
        if self.rightChild == None:
            self.rightChild = BinaryTree(new_child)
        else:
            t = BinaryTree(new_child)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
