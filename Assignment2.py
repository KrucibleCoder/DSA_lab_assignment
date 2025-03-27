# Problem Statement:
# To create an Abstract Data Type (ADT) that implements "set" concepts.
# a) Add(new element) - Place a value into the set.
# b) Remove(element) - Remove the value from the set.
# c) Contains(element) - Return True if element is in the collection.
# d) Size() - Return the number of values in the collection.
# e) Iterator() - Return an iterator used to loop over the collection.

class SetADT:
    """Class implementing a Set ADT."""
    def __init__(self):
        self.elements = set()
    
    def add_element(self, element):
        """Adds a new element to the set."""
        self.elements.add(element)
    
    def remove_element(self, element):
        """Removes an element from the set if it exists."""
        if element in self.elements:
            self.elements.remove(element)
            return True
        return False
    
    def contains(self, element):
        """Returns True if the element is in the set, else False."""
        return element in self.elements
    
    def size(self):
        """Returns the number of elements in the set."""
        return len(self.elements)
    
    def iterator(self):
        """Returns an iterator over the set."""
        return iter(self.elements)
    
    def display(self):
        """Displays the set elements."""
        print("Set Elements:", self.elements)
    
if __name__ == "__main__":
    set1 = SetADT()
    
    while True:
        print("\nMenu:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Check if element exists")
        print("4. Get size of set")
        print("5. Display set elements")
        print("6. Iterate over set")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter element to add: "))
            set1.add_element(element)
        elif choice == 2:
            element = int(input("Enter element to remove: "))
            if set1.remove_element(element):
                print("Element removed successfully")
            else:
                print("Element not found in the set")
        elif choice == 3:
            element = int(input("Enter element to check: "))
            print("Exists in set:" if set1.contains(element) else "Not in set")
        elif choice == 4:
            print("Size of set:", set1.size())
        elif choice == 5:
            set1.display()
        elif choice == 6:
            print("Iterating over set:")
            for elem in set1.iterator():
                print(elem, end=' ')
            print()
        elif choice == 7:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
