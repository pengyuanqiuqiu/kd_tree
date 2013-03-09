# -*- coding: utf-8 -*-


class Node(object):
	def __init__(self, pos_tuple):
		self._pos_tuple = pos_tuple
		self.left = None
		self.right = None

	def set_data(self, val):
		self._pos_tuple = val

	def get_data(self):
		return self._pos_tuple

def tree_insert(pos_tuple, node, cd, td):
	if node is None:
		node = Node(pos_tuple)
	elif pos_tuple == node.get_data():
		pass
		#print error
	elif pos_tuple[cd] < node.get_data()[cd]:
		node.left = tree_insert(pos_tuple, node.left, (cd + 1) % td, td)
	else :
		node.right = tree_insert(pos_tuple, node.right, (cd + 1) % td, td)
	return node

def likely_nn(pos_tuple, node, cd, td):
	if node is None:
		return []
	elif pos_tuple[cd] < node.get_data()[cd]:
		tmp_ret = likely_nn(pos_tuple, node.left, (cd + 1) % td, td)
	else :
		tmp_ret = likely_nn(pos_tuple, node.right, (cd + 1) % td, td)
	tmp_ret.append(node.get_data())
	return tmp_ret

def minimum(od, *args):
	the_one = None
	for itm in args:
		if itm is None:
			continue
		if the_one is None:
			the_one = itm
		elif the_one[od] > itm[od]:
			the_one = itm
	return the_one

def findmin(node, od, cd, td):
	if node is None:
		return None
	nxt_dim = (cd + 1) % td
	if cd == od:
		if node.left is None:
			return node.get_data()
		else :
			return findmin(node.left, od, nxt_dim, td)
	else :
		return minimum(od, findmin(node.left, od, nxt_dim, td), \
				findmin(node.right, od, nxt_dim, td), node.get_data())

def is_equal(t_a, t_b, td):
	for i in xrange(td):
		if t_a[i] != t_b[i]:
			return False
	return True

def tree_delete(pos_tuple, node, cd, td):
	if node is None:
		#node not found
		return
		#raise Exception('pos tuple not found')
	nxt_cd = (cd + 1) % td
	if is_equal(pos_tuple, node.get_data(), td):
		if node.right is not None:
			node.set_data(findmin(node.right, cd, nxt_cd, td))
			node.right = tree_delete(node.get_data(), node.right, nxt_cd, td)
		elif node.left is not None:
			node.set_data(findmin(node.left, cd, nxt_cd, td))
			node.right = tree_delete(node.get_data(), node.left, nxt_cd, td)
			node.left = None
		else :
			node = None
	elif pos_tuple[cd] < node.get_data()[cd]:
		node.left = tree_delete(pos_tuple, node.left, nxt_cd, td)
	else :
		node.right = tree_delete(pos_tuple, node.right, nxt_cd, td)
	return node

def tree_print(node, indent):
	if node is None:
		return
	#print(''.join(['\t' for i in xrange(indent)]), node.get_data())
	tree_print(node.left, indent + 1)
	tree_print(node.right, indent + 1)

#��֧���ص�....
class KDTree(object):
	def __init__(self, dem = 2):
		self._root = None
		self._dem = dem

	def likely_nn(self, pos_tuple):
		return likely_nn(pos_tuple, self._root, 0, self._dem)

	def insert(self, pos_tuple):
		node = tree_insert(pos_tuple, self._root, 0, self._dem)
		if self._root is None:
			self._root = node

	def delete(self, pos_tuple):
		self._root = tree_delete(pos_tuple, self._root, 0, self._dem)

	def print_tree(self):
		tree_print(self._root, 0)

	def find_min(self, dem):
		return findmin(self._root, dem, 0, 2)


'''
if __name__ == '__main__':
	t = KDTree()
	pnt_lst = [(51,75), (25,40), (70,70), (10,30),(35,90), (55,1),(60,80), (1,10), (50,50)]
#	pnt_lst = [(20,20), (10,30), (25,50), (35,25), (30,45), (55,40), (30,35), (45,35), (50,30)]
#	pnt_lst = [(55,40), (45,20), (35,75), (30,25), (60,30), (10, 65), (70,60), (15,10), (70,15), (20,50), (25,85), (80, 90), (25,15)]
#	pnt_lst = [(35,60), (20,45), (60,80), (10,35), (80,40), (20,20), (50,30), (90,60), (70,20), (60,10)]
#	pnt_lst = [(55,40), (45,20), (35,75)]
	for itm in pnt_lst:
		t.insert(itm)
	t.print_tree()
	print t.find_min(0)
	print t.find_min(1)
#	t.print_tree()
	t.delete((35,60))
	t.print_tree()
'''
