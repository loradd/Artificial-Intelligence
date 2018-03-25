
package LoopingString;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.*;

public class LoopingString {

    public static int countOccurrences(String main, String sub) {
        return (main.length() - main.replace(sub, "").length()) / sub.length();
    }

    public static String readFile(String filepath) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(filepath))) {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                line = br.readLine();
            }
            return sb.toString();
        }
    }

    public static void main(String[] args) throws IOException {
        String text = readFile("Lorenzo.txt");
        System.out.printf("Processing String: %s\n", text);
        String patternString = "(.+)\\1+";

        Pattern pattern = Pattern.compile(patternString);
        Matcher matcher = pattern.matcher(text);
        boolean matches = matcher.matches();
        if (matches) {
            /* String is composed by looping substring */
            System.out.printf("Test Response: %b\n", matches); 
            
            /* Printing Looping Substring */
            int result = matcher.groupCount();
            System.out.printf("Looping Substring: %s\n", matcher.group(result)); // Looping Substring : 
            
            /* Printing Looping String Occurrences Count */
            int occurrences = countOccurrences(text, matcher.group(result));
            System.out.printf("Occurrences: %d\n", occurrences);
        } else {
            /* String is not composed by looping substring */
            System.out.printf("Test Response: %b\n", matches); 
        }
        
    }

}
