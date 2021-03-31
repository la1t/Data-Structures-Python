class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        return self.find_in_subtree(self.Root, key)

    def find_in_subtree(self, node, key):
        if key == node.NodeKey:
            find_result = BSTFind()
            find_result.Node = node
            find_result.NodeHasKey = True
            return find_result
        elif key < node.NodeKey:
            if node.LeftChild is None:
                find_result = BSTFind()
                find_result.Node = node
                find_result.NodeHasKey = False
                find_result.ToLeft = True
                return find_result
            return self.find_in_subtree(node.LeftChild, key)
        else:
            if node.RightChild is None:
                find_result = BSTFind()
                find_result.Node = node
                find_result.NodeHasKey = False
                find_result.ToLeft = False
                return find_result
            return self.find_in_subtree(node.RightChild, key)

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, find_result.Node)
        if find_result.Node is None:
            self.Root = new_node
        else:
            if find_result.ToLeft:
                find_result.Node.LeftChild = new_node
            else:
                find_result.Node.RightChild = new_node
        return True
  
    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
        return node
	
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        # 1. находим удаляемый узел
        # 2. находим узел для замены (может не быть)
        # 3. переносим поддерево узла для замены к родителю узла на замену,
        #    переписываем связи с родителем
        # 4. заменяем (или удаляем, если узла на замену нет) удаляемый узел
        # 4.1. переписываем отношения с родителем
        # 4.2. переписываем отношения с правым ребенком
        # 4.3. переписываем отношения с левым ребенком

        # 1.
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False
        node_to_delete = find_result.Node

        SIDE_LEFT = 'left'
        SIDE_RIGHT = 'right'
        SIDE_NONE = 'none'
        if node_to_delete.Parent:
            delete_side = SIDE_RIGHT if node_to_delete.Parent.RightChild == node_to_delete else SIDE_LEFT
        else:
            delete_side = SIDE_NONE
        
        # 2.
        if node_to_delete.RightChild is not None:
            node_to_swap = self.FinMinMax(node_to_delete.RightChild, False)
        elif node_to_delete.LeftChild is not None:
            node_to_swap = self.FinMinMax(node_to_delete.LeftChild, True)
        else:
            node_to_swap = None

        # особый случай: удаляемая нода - лист
        # fixme: deleting root if this is leaf
        if node_to_swap is None:
            if delete_side == SIDE_RIGHT:
                node_to_delete.Parent.RightChild = None
            elif delete_side == SIDE_LEFT:
                node_to_delete.Parent.LeftChild = None
            else:
                self.Root = None
            return True
        
        swap_right = node_to_swap.Parent.RightChild == node_to_swap

        # 3.
        if swap_right:
            node_to_swap.Parent.RightChild = node_to_swap.LeftChild
            if node_to_swap.LeftChild is not None:
                node_to_swap.LeftChild.Parent = node_to_swap.Parent
        else:
            node_to_swap.Parent.LeftChild = node_to_swap.RightChild
            if node_to_swap.RightChild is not None:
                node_to_swap.RightChild.Parent = node_to_swap.Parent

        # 4.1.
        if delete_side == SIDE_RIGHT:
            node_to_delete.Parent.RightChild = node_to_swap
        elif delete_side == SIDE_LEFT:
            node_to_delete.Parent.LeftChild = node_to_swap
        else:
            self.Root = node_to_swap
        node_to_swap.Parent = node_to_delete.Parent

        # 4.2.
        node_to_swap.LeftChild = node_to_delete.LeftChild
        if node_to_swap.LeftChild is not None:
            node_to_swap.LeftChild.Parent = node_to_swap
        
        # 4.3
        node_to_swap.RightChild = node_to_delete.RightChild
        if node_to_swap.RightChild is not None:
            node_to_swap.RightChild.Parent = node_to_swap

        return True

    def Count(self):
        # количество всех узлов в дереве
        if self.Root is None:
            return 0
        return self.count_subtree(self.Root)

    def count_subtree(self, node):
        result = 1
        if node.LeftChild is not None:
            result += self.count_subtree(node.LeftChild)
        if node.RightChild is not None:
            result += self.count_subtree(node.RightChild)
        return result
    
    def WideAllNodes(self):
        if self.Root is None:
            return ()
        res = []
        buffer = [self.Root]
        while len(buffer):
            node = buffer.pop(0)
            res.append(node)
            if node.LeftChild:
                buffer.append(node.LeftChild)
            if node.RightChild:
                buffer.append(node.RightChild)
        return tuple(res)

    IN_ORDER = 0
    POST_ORDER = 1
    PRE_ORDER = 2

    def DeepAllNodes(self, method):
        if not self.Root:
            return ()
        
        if method == BST.IN_ORDER:
            res = self.deep_nodes_in_order(self.Root)
        elif method == BST.POST_ORDER:
            res = self.deep_nodes_post_order(self.Root)
        elif method == BST.PRE_ORDER:
            res = self.deep_nodes_pre_order(self.Root)
        else:
            raise ValueError('unexpected method')

        return tuple(res)

    def deep_nodes_in_order(self, node):
        res = []
        if node.LeftChild:
            res += self.deep_nodes_in_order(node.LeftChild)
        res.append(node)
        if node.RightChild:
            res += self.deep_nodes_in_order(node.RightChild)
        return res

    def deep_nodes_post_order(self, node):
        res = []
        if node.LeftChild:
            res += self.deep_nodes_post_order(node.LeftChild)
        if node.RightChild:
            res += self.deep_nodes_post_order(node.RightChild)
        res.append(node)
        return res
    
    def deep_nodes_pre_order(self, node):
        res = []
        res.append(node)
        if node.LeftChild:
            res += self.deep_nodes_pre_order(node.LeftChild)
        if node.RightChild:
            res += self.deep_nodes_pre_order(node.RightChild)
        return res
