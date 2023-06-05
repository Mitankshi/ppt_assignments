class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    def construct_tree(s, i):
        if i >= len(s) or s[i] == ')':
            return None

        start = i
        while i < len(s) and (s[i].isdigit() or s[i] == '-'):
            i += 1

        val = int(s[start:i])
        node = TreeNode(val)
        
        if i < len(s) and s[i] == '(':
            node.left, i = construct_tree(s, i + 1)

        if i < len(s) and s[i] == '(':
            node.right, i = construct_tree(s, i + 1)

        return node, i + 1

    if not s:
        return None

    root, _ = construct_tree(s, 0)
    return root

s = "4(2(3)(1))(6(5))"
print(str2tree(s=s))