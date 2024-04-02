class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

    def inorder_traversal(root):
        if not root:
            return

        inorder(root.left)
        print(root.key,end="")
        inorder(root.right)

    def delete_deepest(root,d_node):
        q= [root]
        while q:
            temp = q.pop(0)
            if temp is d_node:
                temp= None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)

                if temp.left:
                    if temp.left is d_node:
                        temp.left = None
                        return
                    else:
                        q.append(temp.left)

    def deletion(root,key):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == key:
                return None
            else:
                return root
        key_node=None
        q=[root]
        temp=None
        while q:
            temp = q.pop(0)
            if temp.data==key:
                key_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x=temp.data
            delete_deepest(root,temp)
            key_node.data=x
        return root


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(30)
    root.right = Node(20)