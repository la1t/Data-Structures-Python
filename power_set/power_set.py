# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:
    def __init__(self):
        # ваша реализация хранилища
        self.storage = dict()

    def size(self):
        return len(self.storage)
        # количество элементов в множестве

    def put(self, value):
        # всегда срабатывает
        if value not in self.storage:
            self.storage[value] = True

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return value in self.storage

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        is_exists = value in self.storage
        if is_exists:
            del self.storage[value]
        return is_exists

    def intersection(self, set2):
        # пересечение текущего множества и set2
        result = PowerSet()
        for value in self.get_all_items():
            if set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        # объединение текущего множества и set2
        result = PowerSet()
        for value in self.get_all_items():
            result.put(value)
        for value in set2.get_all_items():
            result.put(value)
        
        return result

    def difference(self, set2):
        # разница текущего множества и set2
        result = PowerSet()
        for value in self.get_all_items():
            if not set2.get(value):
                result.put(value)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for value in set2.get_all_items():
            if not self.get(value):
                return False
        return True
    
    def __eq__(self, o: object) -> bool:
        return self.issubset(o) and o.issubset(self)

    def get_all_items(self):
        return list(self.storage.keys())
