def inorderTraversal(root):
    """
    Inorder traversal
    """
    inorder = []
    if not root:
        return inorder

    nodes = []

    while root or nodes:
        while root:
            nodes.append(root)
            root = root.left

        root = nodes.pop()
        inorder.append(root.val)

        root= root.right

    return inorder
