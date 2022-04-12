package com.udemy.app;

public class App {
	
	/**		Logical Operators
	 * 
	 * 		&&	Logical AND		'A' and 'B' are true
	 * 		||	Logical OR		'A' or 'B' are true
	 * 		!	Logical NOT		Reverse the logical state 
	 * 		^	Logical XOR		'A' or 'B' are true BUT not both
	 * 
	 **/

	public static void main(String[] args) {
		
		int a = 10;
		int b = 20;
		
		//	TRUE && TRUE > TRUE
		if(a < 15 && b > 15) {
			System.out.println("True");
		}
		else {
			System.out.println("False");
		}
		
		//	TRUE || FALSE > TRUE
		if(a < 15 || b > 1000) {
			System.out.println("True");
		}
		else {
			System.out.println("False");
		}
		
		//	!TRUE > FALSE
		if(a != 10) {
			System.out.println("True");
		}
		else {
			System.out.println("False");
		}
		
		//	TRUE ^ TRUE > FALSE
			if(a < 15 ^ b > 15) {
				System.out.println("True");
			}
			else {
				System.out.println("False");
			}
			
		//	Example for more than two conditions
		//	TRUE && TRUE && TRUE > TRUE	
			if(a < 15 && b > 15 && b != 21) {
				System.out.println("True");
			}
			else {
				System.out.println("False");
			}			
	}
}
