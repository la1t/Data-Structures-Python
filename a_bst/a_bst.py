class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = self.calc_tree_size(depth)
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        current_index = 0
        while self.check_in_bounds(current_index):
            if self.Tree[current_index] is None:
                return -current_index
            elif self.Tree[current_index] == key:
                return current_index
            elif self.Tree[current_index] > key:
                current_index = self.get_left_child_index(current_index)
            else:
                current_index = self.get_right_child_index(current_index)

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index >= 0:
            return index
        self.Tree[-index] = key
        return -index

    @staticmethod
    def calc_tree_size(depth):
        return sum(2 ** n for n in range(depth + 1))
    
    @staticmethod
    def get_left_child_index(index):
        return index * 2 + 1
    
    @staticmethod
    def get_right_child_index(index):
        return index * 2 + 2
    
    def check_in_bounds(self, index):
        return index < len(self.Tree)


class FindResult:
    def __init__(self, index, is_found):
        self.index = index
        self.is_found = is_found
