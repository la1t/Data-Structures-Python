class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
    
    def add_childs(self, left_child=None, right_child=None):
        self.LeftChild = left_child
        self.RightChild = right_child
    
    def count_subnodes(self):
        res = 1
        if self.LeftChild is not None:
            res += self.LeftChild.count_subnodes()
        if self.RightChild is not None:
            res += self.RightChild.count_subnodes()
        return res
    
    def is_subtree_balanced(self):
        left_count = self.LeftChild.count_subnodes() if self.LeftChild else 0
        right_count = self.RightChild.count_subnodes() if self.RightChild else 0
        if abs(left_count - right_count) > 1:
            return False
        if self.LeftChild and not self.LeftChild.is_subtree_balanced():
            return False
        if self.RightChild and not self.RightChild.is_subtree_balanced():
            return False
        return True
        

class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        if not a:
            return
        self.Root = self.fill_tree(None, sorted(a))
        
    def fill_tree(self, parent_node, a):
        if not a:
            return
        mid_index = len(a) // 2
        new_node = BSTNode(a[mid_index], parent_node)
        new_node.LeftChild = self.fill_tree(new_node, a[:mid_index])
        new_node.RightChild = self.fill_tree(new_node, a[mid_index + 1:])
        return new_node

    def IsBalanced(self, root_node):
        return root_node.is_subtree_balanced()
