

def is_BST(root):
    """
    Validate BST
    """
    if not root:
        return True

    stack = []
    prev_node = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev and prev.val >= root.val:
            return False

        prev= root
        root= root.right

    return True
