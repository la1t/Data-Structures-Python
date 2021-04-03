class Heap:
    # fixme: empty heaps

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
		
    def MakeHeap(self, a, depth):
	    # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 
        self.HeapArray = [None] * self.calc_array_len(depth)
        for key in a:
            self.Add(key)

    def GetMax(self):
        if self.is_empty():
            return -1
        result = self.HeapArray[0]
        last_index = self.last_index()
        self.HeapArray[0] = self.HeapArray[last_index]
        self.HeapArray[last_index] = None
        self.sift_down(0)
        return result

    def Add(self, key):
        free_index = self.first_free_index()
        if free_index is None:
            return False
        self.HeapArray[free_index] = key
        self.sift_up(free_index)
        return True
    
    def sift_down(self, i):
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)

        if not self.exists(left_child) and not self.exists(right_child):
            return
        elif not self.exists(left_child):
            max_child = right_child
        elif not self.exists(right_child):
            max_child = left_child
        else:
            max_child = max(left_child, right_child, key=lambda i: self.HeapArray[i])
        
        if self.HeapArray[max_child] > self.HeapArray[i]:
            self.HeapArray[max_child], self.HeapArray[i] = self.HeapArray[i], self.HeapArray[max_child]
            self.sift_down(max_child)
        
    
    def sift_up(self, i):
        parent = self.get_parent(i)
        if not self.check_boundaries(parent):
            return
        if self.HeapArray[parent] < self.HeapArray[i]:
            self.HeapArray[parent], self.HeapArray[i] = self.HeapArray[i], self.HeapArray[parent]
            self.sift_up(parent)
    
    @staticmethod
    def get_left_child(i):
        return 2 * i + 1
    
    @staticmethod
    def get_right_child(i):
        return 2 * i + 2
    
    @staticmethod
    def get_parent(i):
        return (i - 1) // 2
    
    def check_boundaries(self, i):
        return 0 <= i < len(self.HeapArray)
    
    def exists(self, i):
        return self.check_boundaries(i) and self.HeapArray[i] is not None

    def first_free_index(self):
        for i, key in enumerate(self.HeapArray):
            if key is None:
                return i
        return None
    
    def last_index(self):
        free_index = self.first_free_index()
        if free_index is None:
            return len(self.HeapArray) - 1
        elif free_index == 0:
            return None
        else:
            return free_index - 1
        
    def is_empty(self):
        return len(self.HeapArray) == 0 or self.HeapArray[0] is None
    
    @staticmethod
    def calc_array_len(depth):
        return 2 ** (depth + 1) - 1
