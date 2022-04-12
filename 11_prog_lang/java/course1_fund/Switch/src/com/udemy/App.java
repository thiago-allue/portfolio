package com.udemy;

public class App {

	public static void main(String[] args) {
		
		String name = "Kevin";
		
		switch(name) {
			case "Adam": System.out.println("Hi Adam!");
				break;
			case "Kevin": System.out.println("Hello Kevin!");
				break;
			default: System.out.println("I do not know your name");
				break;
		}
		
	}
}
