class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# Root node
root = TreeNode("A")

# Child nodes
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")


root.children.append(b)
root.children.append(c)
root.children.append(d)


b.children.append(TreeNode("E"))
b.children.append(TreeNode("F"))


c.children.append(TreeNode("G"))


def print_tree(node, level=0):
    print("  " * level + str(node.value))
    for child in node.children:
        print_tree(child, level + 1)


print_tree(root)
