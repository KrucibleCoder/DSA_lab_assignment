class HashTable:
    """
    A Hash Table implementation with support for different collision resolution techniques.
    Supported methods: Linear Probing, Quadratic Probing, and Double Hashing.
    """
    def __init__(self, size, collision_resolution):
        self.size = size
        self.table = [None] * size  # Initialize hash table with None
        self.collision_resolution = collision_resolution  # Set collision resolution method
    
    def hash_function(self, key):
        """Computes the primary hash index for a given key."""
        return key % self.size
    
    def linear_probing(self, index):
        """Handles collisions using Linear Probing."""
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Move to next slot
        return index
    
    def quadratic_probing(self, index, key):
        """Handles collisions using Quadratic Probing."""
        i = 1
        while self.table[(index + i ** 2) % self.size] is not None:
            i += 1
        return (index + i ** 2) % self.size
    
    def double_hashing(self, index, key):
        """Handles collisions using Double Hashing."""
        step = 7 - (key % 7)  # Secondary hash function
        while self.table[index] is not None:
            index = (index + step) % self.size  # Move by step size
        return index
    
    def insert(self, key, value):
        """Inserts a key-value pair into the hash table."""
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            print(f"Collision detected at index {index} for key {key}.")
            # Resolve collision based on the selected method
            if self.collision_resolution == 'linear':
                index = self.linear_probing(index)
            elif self.collision_resolution == 'quadratic':
                index = self.quadratic_probing(index, key)
            elif self.collision_resolution == 'double':
                index = self.double_hashing(index, key)
            self.table[index] = (key, value)
    
    def search(self, key):
        """Searches for a key in the hash table and returns its value if found."""
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return None  # Key not found
            if self.table[index][0] == key:
                return self.table[index][1]  # Return the value
            index = (index + 1) % self.size  # Move to next slot (Linear probing for search)
        return None
    
    def delete(self, key):
        """Deletes a key from the hash table if present."""
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return False  # Key not found
            if self.table[index][0] == key:
                self.table[index] = None  # Remove the entry
                return True
            index = (index + 1) % self.size  # Move to next slot
        return False
    
    def display(self):
        """Displays the hash table contents."""
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
