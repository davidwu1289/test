import java.io.*;

public class CloneFile {
    public static void main(String[] args) {
        String originalFilePath = "original_file.txt";
        String clonedFilePath = "cloned_file.txt";
        int totalRecords = 10000000;
        int recordCount = 20;

        int timesToWrite = totalRecords / recordCount;

        try (BufferedReader reader = new BufferedReader(new FileReader(originalFilePath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(clonedFilePath))) {

            String[] originalContent = new String[recordCount];
            for (int i = 0; i < recordCount; i++) {
                originalContent[i] = reader.readLine();
            }

            for (int i = 0; i < timesToWrite; i++) {
                for (String line : originalContent) {
                    writer.write(line);
                    writer.newLine();
                }
            }

            System.out.println(totalRecords + " records have been written to " + clonedFilePath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

