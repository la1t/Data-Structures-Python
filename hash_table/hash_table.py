class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
         value_bytes = list(value.encode('utf-8'))
         return sum(value_bytes) % self.size

    def seek_slot(self, value):
        value_hash = self.hash_fun(value)
        slot = value_hash
        while self.slots[slot] is not None:
            slot = self.make_step(slot)
            if slot == value_hash:
                return None
        return slot

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        value_hash = self.hash_fun(value)
        slot = value_hash
        while self.slots[slot] != value:
            if self.slots[slot] is None:
                return None
            slot = self.make_step(slot)
            if slot == value_hash:
                return None
        return slot
    
    def make_step(self, slot):
        return (slot + self.step) % self.size
