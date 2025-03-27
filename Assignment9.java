// Problem Statement: Assume we have two input and two output tapes to perform the sorting. 
// The internal memory can hold and sort m records at a time. 
// Write a program in Java for external sorting. Find out the time complexity.

import java.io.*;
import java.util.*;

class ExternalSort {
    private static final int CHUNK_SIZE = 5; // Size of internal memory (adjust as needed)
    
    // Function to split the large file into sorted chunks
    public static List<File> splitAndSortChunks(String inputFile) throws IOException {
        List<File> sortedFiles = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(inputFile));
        List<Integer> chunk = new ArrayList<>();
        String line;

        while ((line = reader.readLine()) != null) {
            chunk.add(Integer.parseInt(line));

            // If chunk reaches its maximum size, sort and store it
            if (chunk.size() == CHUNK_SIZE) {
                sortedFiles.add(writeSortedChunk(chunk));
                chunk.clear();
            }
        }

        // Process the last chunk if it exists
        if (!chunk.isEmpty()) {
            sortedFiles.add(writeSortedChunk(chunk));
        }

        reader.close();
        return sortedFiles;
    }

    // Function to write sorted chunks to temporary files
    private static File writeSortedChunk(List<Integer> chunk) throws IOException {
        Collections.sort(chunk);
        File tempFile = File.createTempFile("sortedChunk", ".txt");
        tempFile.deleteOnExit();

        BufferedWriter writer = new BufferedWriter(new FileWriter(tempFile));
        for (int num : chunk) {
            writer.write(num + "\n");
        }

        writer.close();
        return tempFile;
    }

    // Function to merge sorted chunks into the final sorted output file
    public static void mergeSortedChunks(List<File> sortedFiles, String outputFile) throws IOException {
        PriorityQueue<FileEntry> minHeap = new PriorityQueue<>();
        List<BufferedReader> readers = new ArrayList<>();

        // Initialize heap with the first line of each sorted chunk
        for (File file : sortedFiles) {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            readers.add(reader);
            String line = reader.readLine();
            if (line != null) {
                minHeap.add(new FileEntry(Integer.parseInt(line), reader));
            }
        }

        BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile));

        while (!minHeap.isEmpty()) {
            FileEntry entry = minHeap.poll();
            writer.write(entry.value + "\n");

            // Read next line from the same file
            String line = entry.reader.readLine();
            if (line != null) {
                minHeap.add(new FileEntry(Integer.parseInt(line), entry.reader));
            }
        }

        // Close all resources
        writer.close();
        for (BufferedReader reader : readers) {
            reader.close();
        }
    }

    // Helper class for managing priority queue in merge step
    static class FileEntry implements Comparable<FileEntry> {
        int value;
        BufferedReader reader;

        public FileEntry(int value, BufferedReader reader) {
            this.value = value;
            this.reader = reader;
        }

        @Override
        public int compareTo(FileEntry other) {
            return Integer.compare(this.value, other.value);
        }
    }

    // Main function to execute external sort
    public static void main(String[] args) throws IOException {
        String inputFile = "input.txt";
        String outputFile = "sorted_output.txt";

        // Step 1: Split input file into sorted chunks
        List<File> sortedChunks = splitAndSortChunks(inputFile);

        // Step 2: Merge sorted chunks into final sorted output
        mergeSortedChunks(sortedChunks, outputFile);

        System.out.println("Sorting completed. Check " + outputFile);
    }
}
