import unittest

from binary_tree import BinaryTree

class TestBunaryTreeMethods(unittest.TestCase):

    def test_balanced(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        self.assertTrue(root.is_tree_balanced())

    def test_balanced_left(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.left.right = BinaryTree(19)

        self.assertTrue(root.is_tree_balanced())

    def test_balanced_right(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(19)

        self.assertTrue(root.is_tree_balanced())

    def test_not_balanced_left(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.left.right.left = BinaryTree(6)

        self.assertFalse(root.is_tree_balanced())
    
    def test_not_balanced_right(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.left = BinaryTree(3)
        root.right.left = BinaryTree(4)
        root.right.right = BinaryTree(5)
        root.right.right.left = BinaryTree(6)

        self.assertFalse(root.is_tree_balanced())
    
    def test_get_height(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(19)

        self.assertEqual(root.get_height(), 3)

    def test_get_balance(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(19)

        self.assertEqual(root.get_balance(), 1)

if __name__ == "__main__":
    unittest.main()