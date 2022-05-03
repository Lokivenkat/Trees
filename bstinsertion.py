class node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class tree:
    def createnode(self,data):
        return node(data)
    def insert(self,node,data):
        if(node is None):
            return(self.createnode(data))
        if(data<node.data):
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return(node)
    def inorder(self,root):
        if(root is not None):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if(root is not None):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root is not None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    
t=tree()
root=t.createnode(5)
print(root.data)
t.insert(root,2)
t.insert(root,10)
t.insert(root,7)
t.insert(root,15)
t.insert(root,12)
t.insert(root,20)
t.insert(root,30)
t.insert(root,6)
t.insert(root,8)
t.inorder(root)
print()
t.preorder(root)
print()
t.postorder(root)
print()

        
