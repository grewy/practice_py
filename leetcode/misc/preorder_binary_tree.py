

def preOrder(root):
    """
    Pre-order traversal of tree
    """
    if not root:
        return

    stack  = []
    result =[]

    stack.append(root)

    while stack:
        curr = stack.pop()

        if curr:
            stack.append(curr.right)
            stack.append(curr.left)

            result.append(curr.val)

    return result

