// Problem Statement: Implement shell sort algorithm in JAVA demonstrating 
// shell data structure with modularity of programming language.

import java.util.Scanner;

class ShellSort {
    
    // Function to perform Shell Sort
    public static void shellSort(int[] arr) {
        int n = arr.length;
        
        // Start with a large gap and reduce it
        for (int gap = n / 2; gap > 0; gap /= 2) {
            
            // Perform gapped insertion sort for this gap size
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;
                
                // Shift elements to find correct position for arr[i]
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                
                // Place temp at its correct position
                arr[j] = temp;
            }
        }
    }

    // Function to display the array
    public static void displayArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Main function
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking user input
        System.out.print("Enter number of elements: ");
        int n = scanner.nextInt();
        
        int[] arr = new int[n];
        
        System.out.println("Enter elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.println("\nOriginal Array:");
        displayArray(arr);
        
        // Sorting the array using Shell Sort
        shellSort(arr);

        System.out.println("\nSorted Array using Shell Sort:");
        displayArray(arr);
        
        scanner.close();
    }
}
