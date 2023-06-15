
import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size, num_hash_functions):
        self.size = size
        self.num_hash_functions = num_hash_functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.num_hash_functions):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        for seed in range(self.num_hash_functions):
            index = mmh3.hash(item, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True


bloom_filter = BloomFilter(100, 3)

# Add items to the filter
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# Check if items are in the filter
print(bloom_filter.contains("apple"))    # True
print(bloom_filter.contains("banana"))   # True
print(bloom_filter.contains("orange"))   # True
print(bloom_filter.contains("grape"))    # False (not added to the filter)


