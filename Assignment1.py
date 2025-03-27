# Problem Statement:
# Consider a telephone book database of N clients. Implement a hash table to quickly look up a client's telephone number.
# Use two collision handling techniques and compare them based on the number of comparisons required to find a set of telephone numbers.

class HashTable:
    """Class representing a hash table for storing telephone book entries."""
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.comparisons = 0  # To count comparisons for analysis
    
    def hash_function(self, key):
        """Simple hash function using modulo."""
        return key % self.size
    
    def linear_probing(self, key, phone_number):
        """Handles collision using linear probing."""
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            self.comparisons += 1
            if index == original_index:
                print("Table is full!")
                return
        self.table[index] = (key, phone_number)
    
    def quadratic_probing(self, key, phone_number):
        """Handles collision using quadratic probing."""
        index = self.hash_function(key)
        i = 1
        while self.table[index] is not None:
            index = (self.hash_function(key) + i ** 2) % self.size
            self.comparisons += 1
            i += 1
            if i == self.size:
                print("Table is full!")
                return
        self.table[index] = (key, phone_number)
    
    def search(self, key, method="linear"):
        """Searches for a phone number using the given method."""
        index = self.hash_function(key)
        i = 0
        self.comparisons = 0
        
        while self.table[index] is not None:
            self.comparisons += 1
            if self.table[index][0] == key:
                return self.table[index][1], self.comparisons
            
            if method == "linear":
                index = (index + 1) % self.size
            else:
                i += 1
                index = (self.hash_function(key) + i ** 2) % self.size
            
            if i == self.size:
                break
        return None, self.comparisons
    
    def display(self):
        """Displays the hash table contents."""
        for i, entry in enumerate(self.table):
            print(f"Index {i}: {entry}")
    
if __name__ == "__main__":
    size = int(input("Enter size of hash table: "))
    hash_table = HashTable(size)
    
    while True:
        print("\nMenu:")
        print("1. Insert using Linear Probing")
        print("2. Insert using Quadratic Probing")
        print("3. Search a number")
        print("4. Display Hash Table")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter client ID: "))
            phone = input("Enter phone number: ")
            hash_table.linear_probing(key, phone)
        elif choice == 2:
            key = int(input("Enter client ID: "))
            phone = input("Enter phone number: ")
            hash_table.quadratic_probing(key, phone)
        elif choice == 3:
            key = int(input("Enter client ID to search: "))
            method = input("Enter search method (linear/quadratic): ").strip().lower()
            phone, comparisons = hash_table.search(key, method)
            if phone:
                print(f"Phone Number: {phone}, Comparisons: {comparisons}")
            else:
                print("Client not found")
        elif choice == 4:
            hash_table.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
