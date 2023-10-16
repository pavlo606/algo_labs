class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_height(self) -> int:
        left, right = 0, 0
        if self.left:
            left = self.left.get_height()
        if self.right:
            right = self.right.get_height()

        return max(left, right) + 1

    def get_balance(self) -> int:
        return self.right.get_height() - self.left.get_height()

    def is_tree_balanced(self) -> bool:
        if abs(self.get_balance()) <= 1:
            return True
        else:
            return False

    def print(self) -> str:
        if self.left:
            self.left.print()
        print(self.value, end=" ")
        if self.right:
            self.right.print()

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.right.left = BinaryTree(6)

print(root.is_tree_balanced())
root.print()