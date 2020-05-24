

def helper(low, high):
    if low > high:
        return

    root = TreeNode(preorder.pop(0))
    idx =

def build(preorder, inorder):

    def helper(low, high):
        if low > high:
            return

        root = TreeNode(preorder.pop(0))
        idx = inorder_index_map[root.val]
        root.left = helper(low, idx - 1)
        root.right = helper(idx+1, high)

        return root

    inorder_index_map = {}
    for k, v in enumerate(inorder):
        inorder_index_map[v] = k

    return helper(0, len(preorder)-1)
