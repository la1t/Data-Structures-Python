class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
    
    def put(self, key, value):
        key_slot = self.find_key_slot(key)
        if key_slot is None:
            key_slot = self.seek_slot(key)
            self.hits[key_slot] = 0
        
        self.slots[key_slot] = key
        self.values[key_slot] = value
    
    def is_key(self, key):
        slot = self.find_key_slot(key)
        if slot is not None:
            self.hits[slot] += 1
            return True
        return False
    
    def get(self, key):
        slot = self.find_key_slot(key)
        if slot is not None:
            self.hits[slot] += 1
            return self.values[slot]
        return None
    
    def find_key_slot(self, key):
        key_hash = self.hash_fun(key)
        slot = key_hash
        while self.slots[slot] != key:
            if self.slots[slot] is None:
                return None
            slot = self.make_step(slot)
            if slot == key_hash:
                return None
        return slot
    
    def hash_fun(self, value):
        value_bytes = list(value.encode('utf-8'))
        return sum(value_bytes) % self.size
    
    def seek_slot(self, value):
        value_hash = self.hash_fun(value)
        slot = value_hash
        while self.slots[slot] is not None:
            slot = self.make_step(slot)
            if slot == value_hash:
                return self.find_min_hit_slot()
        return slot
    
    def make_step(self, slot):
        return (slot + 1) % self.size
    
    def find_min_hit_slot(self):
        return self.hits.index(min(self.hits))
