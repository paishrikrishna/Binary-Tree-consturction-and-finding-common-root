root_objs=[]
ROOT=['A','B','C','D','E','F','G']
LEFT = ['B','C','NULL','NULL','F','NULL','NULL']
RIGHT = ['E','D','NULL','NULL','G','NULL','NULL']
c_a,c_b="null","null"
class tree:
	def __init__(self):
		self.root="null"
		self.left="null"
		self.right="null"

def build_tree(root,left,right):
	obj = tree()
	obj.root = root
	obj.left = left
	obj.right = right
	global root_objs
	root_objs.append(obj)

def main():
	for i in range(len(ROOT)):
		build_tree(ROOT[i],LEFT[i],RIGHT[i])

def common_ancestor(r_a,r_b):
	
	for i in root_objs:
		if i.left == r_a or i.right == r_a:
			global c_a
			c_a = i.root
		if i.left == r_b or i.right == r_b:
			global c_b
			c_b = i.root
		if c_a != "null" and c_b != "null":
			break
	return c_a,c_b



if __name__ == "__main__":
	main()
	c_a,c_b = common_ancestor("G","F")
	while(c_a!=c_b):
		c_a,c_b = common_ancestor(c_a,c_b)
	print(c_a)