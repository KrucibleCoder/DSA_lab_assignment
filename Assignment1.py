class HashTable:
    def __init__(self, size, collision_resolution):
        self.size = size
        self.table = [None] * size  # Using None to handle open addressing
        self.collision_resolution = collision_resolution
    
    def hash_function(self, key):
        return key % self.size
    
    def linear_probing(self, index):
        while self.table[index] is not None:
            index = (index + 1) % self.size
        return index
    
    def quadratic_probing(self, index, key):
        i = 1
        while self.table[(index + i ** 2) % self.size] is not None:
            i += 1
        return (index + i ** 2) % self.size
    
    def double_hashing(self, index, key):
        step = 7 - (key % 7)  # Second hash function
        while self.table[index] is not None:
            index = (index + step) % self.size
        return index
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            print(f"Collision detected at index {index} for key {key}.")
            if self.collision_resolution == 'linear':
                index = self.linear_probing(index)
            elif self.collision_resolution == 'quadratic':
                index = self.quadratic_probing(index, key)
            elif self.collision_resolution == 'double':
                index = self.double_hashing(index, key)
            self.table[index] = (key, value)
    
    def search(self, key):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return None
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size  # Linear probing for search
        return None  # Key not found
    
    def delete(self, key):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return False
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size  # Linear probing for deletion
        return False  # Key not found
    
    def display(self):
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value}")
    
if __name__ == "__main__":
    size = int(input("Enter hash table size: "))
    print("Select collision resolution method: linear, quadratic, or double")
    method = input("Enter method: ").strip().lower()
    
    ht = HashTable(size, method)
    
    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter key: "))
            value = input("Enter value: ")
            ht.insert(key, value)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            result = ht.search(key)
            print(f"Value found: {result}" if result else "Key not found")
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            if ht.delete(key):
                print("Key deleted successfully")
            else:
                print("Key not found")
        elif choice == 4:
            ht.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
