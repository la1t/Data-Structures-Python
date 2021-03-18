class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.storage = 0

    def hash1(self, str1):
        # 17
        modifier = 17
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * modifier + code) % self.filter_len
        return result

    def hash2(self, str1):
        # 223 
        modifier = 223
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * modifier + code) % self.filter_len
        return result

    def add(self, str1):
        self.storage |= self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1):
        mask = self.hash1(str1) | self.hash2(str1)
        return self.storage & mask == mask
