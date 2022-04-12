package com.udemy;

public class App {

	/**
	 * We can pass a parameter by reference and by value
	 * 
	 * 	- by reference: the caller and the callee use the same variable
	 * 		for the parameter. If we modify the variable the effect is visible
	 * 			to the caller's method
	 * 
	 * 		Java passes all objects by reference: array
	 * 
	 * 	- by value: caller and callee have two different independent variables
	 * 		with the same value. If we modify the variable the effect is NOT visible
	 * 			to the caller's method 
	 * 
	 * 		Java passes all primitive data type by value: int, char, float...
	 * 
	 * 		public void swap(int num1, int num2) {
	 * 			int temp = num1;
	 * 			num1 = num2;
	 * 			num2 = temp;
	 * 		}
	 */
	
	public static void main(String[] args) {
		
//		int num1 = 10;
//		int num2 = 20;
		
		Person person = new Person();
		person.setAge(20);
		
		System.out.println("Before calling change() method: age="+person.getAge());
		
		change(person);
		
		System.out.println("After calling change() method: age="+person.getAge());
	}
	
//	public static void change(int num1, int num2) {
//		int temp = num1;
//		num1 = num2;
//		num2 = temp;
//	}
	
	public static void change(Person p) {
		p.setAge(30);
	}
}
