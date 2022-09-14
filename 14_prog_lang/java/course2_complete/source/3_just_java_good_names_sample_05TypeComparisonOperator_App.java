package com.udemy.app;

public class App {

	/**
	 * Type Comparison Operator is also known as the instanceof operator
	 * 
	 * The instanceof operator compares an object to a specified type and returns true if the type of object and
	 * the specified type are the same.
	 * 
	 * if (objectReference instanceof type)
	 * 
	 **/

	public static void main(String[] args) {

		/**
		 * example1
		 **/
		String testSubject = "apple";

		boolean testResult = testSubject instanceof String;

		System.out.println("The result of the test example1: " + testResult);

		/**
		 * example2
		 **/

		ChildClass child = new ChildClass();

		boolean testResult2 = child instanceof App;

		System.out.println("The result of the test example2: " + testResult2);
	}
}
