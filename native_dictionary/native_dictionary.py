class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        key_bytes = list(key.encode('utf-8'))
        return sum(key_bytes) % self.size

    def is_key(self, key):
        return self.find_key_slot(key) is not None

    def put(self, key, value):
        key_slot = self.find_key_slot(key)
        if key_slot is None:
            key_slot = self.seek_slot(key)
            if key_slot is None:
                raise ValueError
        
        self.slots[key_slot] = key
        self.values[key_slot] = value

    def get(self, key):
        slot = self.find_key_slot(key)
        return self.values[slot] if slot is not None else None
    
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

    def seek_slot(self, value):
        value_hash = self.hash_fun(value)
        slot = value_hash
        while self.slots[slot] is not None:
            slot = self.make_step(slot)
            if slot == value_hash:
                return None
        return slot

    def make_step(self, slot):
        return (slot + 1) % self.size
