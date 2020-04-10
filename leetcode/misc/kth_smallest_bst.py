
def kth_smallest_bst(root, k):
    """
    Find kth smallest element in BST
    """
    stack = []

    # Go left
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val

        root= root.right

    return -1
