package com.udemy.app;

public class App {

	public static void main(String[] args) {

		/**
		 * Ternary Operator
		 * 
		 * result = testCondition ? value1 : value2
		 * 
		 **/

		// first, basic example
		int a = 10;
		int b;
		b = a < 20 ? 22 : 33;
		System.out.println(b);

		// second, smaller of two values example
		int smallerValue;
		int c = 3;
		int d = 2;
		smallerValue = c < d ? c : d;
		System.out.println("Smaller value = " + smallerValue);

		/**
		 * Ternary operator with more than one condition
		 *
		 * result = testCondition1 ? value1 : testCondition2 ? value2 : value3
		 *
		 **/

		// example
		int e = 9; // int e = 0
		System.out.println(e == 0 ? "zero" : e < 0 ? "negative number" : "positive number");

		/**
		 * The example above is appropriate, but keep in mind: Do not use too long and complex chained ternary
		 * statements. Code readability is important!
		 * 
		 **/
	}
}
