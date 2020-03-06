
#Define class Node
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.data)

#function to find a level
def findLevel(root, node, level):
	if not root:
		return None

	if root.data == node:
		return level + 1

	left = findLevel(root.left, node, level + 1)
	right = findLevel(root.right, node, level + 1)

	if not left and not right:
		return None
	elif left:
		return left
	else:
		return right

# Function to find lca of given nodes n1 and n2 where

def find_lca_node(root, n1, n2):
	if not root or n1 == root.data or root.data == n2:
		return root

	lca_left = find_lca_node(root.left, n1, n2)
	lca_right = find_lca_node(root.right, n1, n2)

	if lca_left and lca_right:
		return root

	return lca_right if lca_right else lca_left

# Function to find distnce between two nodes in a binary tree
def findDistance(root, n1, n2):
	level_n1 = findLevel(root, n1, 0)
	if not level_n1:
		print("Node", n1, "does not exists in the binary tree")
		return

	level_n2 = findLevel(root, n2, 0)
	if not level_n2:
		print("Node", n2, "does not exists in the binary tree")
		return

	lca = find_lca_node(root, n1, n2)
	level_lca = findLevel(root, lca.data, 0)

	print("The distance between node", n1, "and node", n2, "is", \
			level_n1 + level_n2 - 2 * level_lca)

#Design Binary tree
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
	
#find distance
findDistance(root, 1, 3)
findDistance(root, 3, 6)
findDistance(root, 4, 6)
	
