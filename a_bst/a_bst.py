class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = self.calc_tree_size(depth)
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        find_result = self.find(key)
        return find_result.index if find_result.is_found else None

    def find(self, key):
        current_index = 0
        while self.check_in_bounds(current_index):
            if self.Tree[current_index] is None:
                return FindResult(current_index, False)
            elif self.Tree[current_index] == key:
                return FindResult(current_index, True)
            elif self.Tree[current_index] > key:
                current_index = self.get_left_child_index(current_index)
            else:
                current_index = self.get_right_child_index(current_index)
        return FindResult(None, False)

    def AddKey(self, key):
        find_result = self.find(key)
        if find_result.is_found:
            return find_result.index
        if find_result.index is None:
            return -1
        self.Tree[find_result.index] = key
        return find_result.index

    @staticmethod
    def calc_tree_size(depth):
        return sum(2 ** n for n in range(depth))
    
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
