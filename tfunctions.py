class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1


class Tree:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return self.inorder(self.head)

    def inorder(self, head):
        if head is None:
            return

        yield head.value

        yield from self.inorder(head.left)
        yield from self.inorder(head.right)


def bst_generator(head):
    if head.left is not None:
        yield from bst_generator(head.left)
    yield head
    if head.right is not None:
        yield from bst_generator(head.right)
