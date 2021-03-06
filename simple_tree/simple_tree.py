class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
        self.Level = None
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
        if root is not None:
            self.Root.Level = 0
	
    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        NewChild.Level = ParentNode.Level + 1
        ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []
        result = self.get_all_nodes_for_subtree(self.Root)
        return result

    def get_all_nodes_for_subtree(self, node):
        result = [node]
        for child in node.Children:
            result += self.get_all_nodes_for_subtree(child)
        return result

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if self.Root is None:
            return []
        result = self.find_nodes_by_value_for_subtree(self.Root, val)
        return result
    
    def find_nodes_by_value_for_subtree(self, node, val):
        result = []
        if node.NodeValue == val:
            result.append(node)
        for child in node.Children:
            result += self.find_nodes_by_value_for_subtree(child, val)
        return result
   
    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        # количество всех узлов в дереве
        if self.Root is None:
            return 0
        return self.count_subtree(self.Root)

    def count_subtree(self, node):
        result = 1
        for child in node.Children:
            result += self.count_subtree(child)
        return result

    def LeafCount(self):
        # количество листьев в дереве
        if self.Root is None:
            return 0
        return self.leaf_count_subtree(self.Root)

    def leaf_count_subtree(self, node):
        if not node.Children:
            return 1
        result = 0
        for child in node.Children:
            result += self.leaf_count_subtree(child)
        return result
    
    def WideAllNodes(self):
        pass

    def EvenTrees(self):
        """
        1. Обрезаем все четные поддеревья из корня
        Для всех обрезанных поддеревьев запускаем EvenTrees, добавляем к результату 
        """
        # fixme: нечетное дерево
        result = []
        for child in self.Root.Children:
            subtree = SimpleTree(child)
            if subtree.Count() % 2 == 0:
                result += [self.Root, child]
            result += subtree.EvenTrees()
        return result
