// Problem Statement: Department maintains a student information system with roll number, name, 
// division, and address. The program allows adding, deleting, and searching for student records
// in a sequential file.

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Structure to store student information
struct Student {
    int rollNumber;
    string name;
    string division;
    string address;
};

// Function to add a new student record
void addStudent() {
    ofstream outFile("students.txt", ios::app); // Append mode to avoid overwriting
    if (!outFile) {
        cout << "Error opening file!" << endl;
        return;
    }

    Student s;
    cout << "Enter Roll Number: ";
    cin >> s.rollNumber;
    cin.ignore(); // Ignore newline character

    cout << "Enter Name: ";
    getline(cin, s.name);
    
    cout << "Enter Division: ";
    getline(cin, s.division);

    cout << "Enter Address: ";
    getline(cin, s.address);

    outFile << s.rollNumber << " " << s.name << " " << s.division << " " << s.address << endl;
    cout << "Student record added successfully.\n";
    
    outFile.close();
}

// Function to display all student records
void displayStudents() {
    ifstream inFile("students.txt");
    if (!inFile) {
        cout << "Error opening file or no records found!" << endl;
        return;
    }

    Student s;
    cout << "\nStudent Records:\n";
    while (inFile >> s.rollNumber) {
        inFile.ignore();
        getline(inFile, s.name, ' ');
        getline(inFile, s.division, ' ');
        getline(inFile, s.address);
        
        cout << "Roll No: " << s.rollNumber << ", Name: " << s.name
             << ", Division: " << s.division << ", Address: " << s.address << endl;
    }
    
    inFile.close();
}

// Function to search for a student by roll number
void searchStudent(int rollNo) {
    ifstream inFile("students.txt");
    if (!inFile) {
        cout << "Error opening file!" << endl;
        return;
    }

    Student s;
    bool found = false;
    while (inFile >> s.rollNumber) {
        inFile.ignore();
        getline(inFile, s.name, ' ');
        getline(inFile, s.division, ' ');
        getline(inFile, s.address);

        if (s.rollNumber == rollNo) {
            cout << "\nStudent Found:\n";
            cout << "Roll No: " << s.rollNumber << ", Name: " << s.name
                 << ", Division: " << s.division << ", Address: " << s.address << endl;
            found = true;
            break;
        }
    }
    
    if (!found) {
        cout << "Student with Roll No " << rollNo << " not found.\n";
    }
    
    inFile.close();
}

// Function to delete a student record
void deleteStudent(int rollNo) {
    ifstream inFile("students.txt");
    ofstream tempFile("temp.txt");

    if (!inFile || !tempFile) {
        cout << "Error opening file!" << endl;
        return;
    }

    Student s;
    bool found = false;

    while (inFile >> s.rollNumber) {
        inFile.ignore();
        getline(inFile, s.name, ' ');
        getline(inFile, s.division, ' ');
        getline(inFile, s.address);

        if (s.rollNumber == rollNo) {
            cout << "Student with Roll No " << rollNo << " deleted successfully.\n";
            found = true;
        } else {
            tempFile << s.rollNumber << " " << s.name << " " << s.division << " " << s.address << endl;
        }
    }

    inFile.close();
    tempFile.close();

    remove("students.txt");
    rename("temp.txt", "students.txt");

    if (!found) {
        cout << "Student with Roll No " << rollNo << " not found.\n";
    }
}

// Main function to provide menu-driven interface
int main() {
    int choice, rollNo;

    do {
        cout << "\nStudent Information System\n";
        cout << "1. Add Student\n";
        cout << "2. Display All Students\n";
        cout << "3. Search Student\n";
        cout << "4. Delete Student\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
                break;
            case 3:
                cout << "Enter Roll Number to search: ";
                cin >> rollNo;
                searchStudent(rollNo);
                break;
            case 4:
                cout << "Enter Roll Number to delete: ";
                cin >> rollNo;
                deleteStudent(rollNo);
                break;
            case 5:
                cout << "Exiting Program.\n";
                break;
            default:
                cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 5);

    return 0;
}
