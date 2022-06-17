package com.udemy;

public class App {

	/**
	 * Abstract classes will hold common functionality 
	 *		for all classes that extend it
	 *	
	 *	For example: all animals move and breathe and reproduce 
	 *			so these can be put into the Animal Class
	 * 
	 * 	abstract keyword:
	 * 		- we can have abstract methods in an abstract class: methods
	 * 				without body
	 * 		- if there is one abstract method: the class should be abstract as well
	 * 		- ABSTRACT CLASSES CANNOT BE INSTANTIATED
	 * 		- a class have to inherit it to be able to use it
	 * 			This class has to implement the abstract methods in the 
	 * 				parent class 
	 * 
	 */
	
	public static void main(String[] args) {
		
		Shape shape = new Rectangle();
		shape.calculateArea();
		
	}
}
