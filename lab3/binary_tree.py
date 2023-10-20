import collections

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_height(self) -> int:
        height = 0

        if self is None:
            return height

        queue = collections.deque()

        queue.append(self)

        while queue:
            currSize = len(queue)
            while currSize > 0:
                currNode = queue.popleft()
                currSize -= 1

                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)

            height += 1
        return height

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

# root = BinaryTree(1)
# root.left = BinaryTree(2)
# root.right = BinaryTree(3)
# root.left.left = BinaryTree(4)
# root.left.right = BinaryTree(5)
# root.left.right.right = BinaryTree(6)
# root.left.right.right.right = BinaryTree(8)
# root.left.right.right.right.right = BinaryTree(11)

root = BinaryTree(50)
root.left = BinaryTree(17)
root.left.left = BinaryTree(9)
root.left.right = BinaryTree(14)
root.left.right.left = BinaryTree(12)
root.left.right = BinaryTree(23)
root.left.right.left = BinaryTree(19)
root.right = BinaryTree(76)
root.right.left = BinaryTree(54)
root.right.left.right = BinaryTree(72)
root.right.left.right.left = BinaryTree(67)



print(root.get_height())
print(root.is_tree_balanced())
print(root.get_balance())
root.print()