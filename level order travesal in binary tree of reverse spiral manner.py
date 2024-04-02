# from collections import deque

# class TreeNode:
#     def __init__(self,data):
#         self.key = data
#         self.left = None
#         self.right = None
#     def inorder_travesral(root):
#         if root:
#             inorder_travesral(root.left)
#             print(root.key, end="")
#             inorder_travesral(root.right)
    
#     def insert(root,key):
#         if not root:
#             return TreeNode(key)
        
#         queue=deque([root])
#         while queue:
#             node = queue.popleft()
            
#             if not node.left:
#                 node.left = TreeNode(key)


from collections import deque

class TreeNode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.key,end="")
            inorder_traversal(root.right)

    def insert(root,key):
        if not root:
            return TreeNode(key)

        queue=deque([root])
        while queue:
            node=queue.popleft()

            if not node.left:
                node.left=TreeNode(key)
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right=TreeNode(key)
                break
            else:
                queue.append(node.right)
