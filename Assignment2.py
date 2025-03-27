class SetADT:
    """
    A Set Abstract Data Type (ADT) that provides basic set operations
    such as union, intersection, and difference.
    """
    def __init__(self):
        """Initializes an empty set."""
        self.elements = set()
    
    def add_element(self, element):
        """Adds an element to the set."""
        self.elements.add(element)
    
    def remove_element(self, element):
        """Removes an element from the set if it exists."""
        if element in self.elements:
            self.elements.remove(element)
            return True
        return False
    
    def union(self, other_set):
        """Returns the union of the current set and another set."""
        return self.elements.union(other_set.elements)
    
    def intersection(self, other_set):
        """Returns the intersection of the current set and another set."""
        return self.elements.intersection(other_set.elements)
    
    def difference(self, other_set):
        """Returns the difference between the current set and another set."""
        return self.elements.difference(other_set.elements)
    
    def display(self):
        """Displays the elements of the set."""
        print("Set Elements:", self.elements)
    
if __name__ == "__main__":
    set1 = SetADT()
    set2 = SetADT()
    
    while True:
        print("\nMenu:")
        print("1. Add element to Set 1")
        print("2. Add element to Set 2")
        print("3. Remove element from Set 1")
        print("4. Remove element from Set 2")
        print("5. Display both sets")
        print("6. Union of sets")
        print("7. Intersection of sets")
        print("8. Difference (Set 1 - Set 2)")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter element to add to Set 1: "))
            set1.add_element(element)
        elif choice == 2:
            element = int(input("Enter element to add to Set 2: "))
            set2.add_element(element)
        elif choice == 3:
            element = int(input("Enter element to remove from Set 1: "))
            if set1.remove_element(element):
                print("Element removed successfully")
            else:
                print("Element not found in Set 1")
        elif choice == 4:
            element = int(input("Enter element to remove from Set 2: "))
            if set2.remove_element(element):
                print("Element removed successfully")
            else:
                print("Element not found in Set 2")
        elif choice == 5:
            print("Set 1:")
            set1.display()
            print("Set 2:")
            set2.display()
        elif choice == 6:
            print("Union of sets:", set1.union(set2))
        elif choice == 7:
            print("Intersection of sets:", set1.intersection(set2))
        elif choice == 8:
            print("Difference (Set 1 - Set 2):", set1.difference(set2))
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
