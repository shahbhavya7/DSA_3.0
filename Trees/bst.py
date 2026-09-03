class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)

        return self._search(root.right, data)




# Example usage:
bst = BST()
# Insert nodes into the BST
for value in [50, 30, 20, 40, 70]:
    bst.insert(value)

# Print the inorder traversal of the BST
print("Inorder traversal of the BST:")
bst.inorder(bst.root)

# Search for a value in the BST
search_value = 40
result = bst.search(search_value)
if result:
    print(f"\nValue {search_value} found in the BST.")
else:
    print(f"\nValue {search_value} not found in the BST.")


        