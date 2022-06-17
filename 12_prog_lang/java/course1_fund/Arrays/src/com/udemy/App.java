package com.udemy;

import java.util.Arrays;
import java.util.Collections;

public class App {

	public static void main(String[] args) {
		
		//String[] names = {"Adam","Kevin","Joe","Daniel","Steven"};
		
		String[] names = new String[3];
		names[0] = "Kevin";
		names[1] = "Joe";
		names[2] = "Adam";
		
		int[] numbers = {1,5,3,-2,10,8};
		
//		for(int i=0;i<=names.length-1;i++) {
//			System.out.println(names[i]);
//		}
		
		Collections.sort(Arrays.asList(names));
		Arrays.sort(numbers);
		
		// for-each loop		
		for(Integer s : numbers) {
			System.out.println(s);
		}
		
	}
}
