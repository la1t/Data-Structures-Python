import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # добавляем объект itm в позицию i, начиная с 0
        # сложность O(n)
        # возможно, имеет смысл обрабатывать вставку в конец массива как отдельную операцию
        # со сложность o(1)
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        
        new_capacity = self.capacity
        if self.count == self.capacity:
            new_capacity *= 2
        new_array = self.make_array(new_capacity)

        for n in range(i):
            new_array[n] = self.array[n]
        
        new_array[i] = itm

        for n in range(i, self.count):
            new_array[n + 1] = self.array[n]
        
        self.array = new_array
        self.capacity = new_capacity
        self.count += 1

    def delete(self, i):
        # удаляем объект в позиции i
        # сложность О(n)
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        new_capacity = self.capacity
        if self.count - 1 < .5 * new_capacity:
            new_capacity = int(new_capacity / 1.5)
        if new_capacity < 16:
            new_capacity = 16
        
        new_array = self.make_array(new_capacity)

        for n in range(i):
            new_array[n] = self.array[n]
        
        for n in range(i + 1, self.count):
            new_array[n - 1] = self.array[n]
        
        self.array = new_array
        self.capacity = new_capacity
        self.count -= 1
