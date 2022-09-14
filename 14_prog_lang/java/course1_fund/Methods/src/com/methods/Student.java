package com.methods;

public class Student {

	private int age;
	private String name;
	
	public Student() {
		
	}
	
	public Student(int age, String name) {
		this.age = age;
		this.name = name;
	}
	
	public String showStudent(int randomNumber) {
		System.out.println("Student name: " + name);
		System.out.println("Student age: " + age);
		System.out.println("Random number: " + randomNumber);
		return "Random number is: " + 2*randomNumber;
	}
}
