package com.udemy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class App {

	public static void main(String[] args) throws IOException {
		
//		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("C:\\Users\\User\\Desktop\\file.txt"));
//		
//		bufferedWriter.write("This is the first line!");
//		bufferedWriter.write(System.lineSeparator());
//		bufferedWriter.write("This is the second line!");
//		
//		bufferedWriter.close();
		
		BufferedReader bufferedReader = new BufferedReader(new FileReader("C:\\Users\\User\\Desktop\\file.txt"));
		
		String line = bufferedReader.readLine();
		
		while( line != null ) {
			System.out.println(line);
			line = bufferedReader.readLine();
		}
		
		bufferedReader.close();
	}
}
