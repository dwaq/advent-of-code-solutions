from anytree import Node, RenderTree

fwft = Node("fwft")
ktlj = Node("ktlj", parent=fwft)
cntj = Node("cntj", parent=fwft)
xhth = Node("xhth", parent=fwft)

for pre, fill, node in RenderTree(fwft):
    print("%s%s" % (pre, node.name))

tknk  = Node("tknk")

fwft.parent = tknk

for pre, fill, node in RenderTree(tknk):
    print("%s%s" % (pre, node.name))