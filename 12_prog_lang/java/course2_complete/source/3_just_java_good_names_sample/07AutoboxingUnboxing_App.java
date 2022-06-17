package com.udemy.app;


public class App {
	
	/**		
	 *		Autoboxing - Unboxing
	 **/

	public static void main(String[] args) {
		
		/**
		 * Autoboxing, primitive -> Object 
		 */

		Integer intObjOldPractice = new Integer(100);  //old practice, don't use it
		
		/**
		 * Number, Boolean, Character constructors, e.g. Integer(int), Boolean(boolean), Character(char) 
		 * are deprecated (not recommended) since version Java 9
		 * 
		 * Oracle says: "The static factory valueOf(int) is generally a better choice, 
		 * as it is likely to yield significantly better space and time performance."
		 */

		Integer intObj = Integer.valueOf(200); 
		
		//without valueOf (valueOf working in the background) same result
		Integer intObj2 = 200;

		System.out.println(intObj);
		
		/**
		 * Unboxing, Object -> primitive 
		 */
		
		int intPrimitive = intObj;
		
		System.out.println(intPrimitive == intObj);
		System.out.println(intPrimitive);
		
		/**
		 * Don't forget that behind the scenes a method is getting called every time when Autoboxing, or Unboxing happen. 
		 * This has a bad effect for performance, especially if many of these happen. 
		 * So autoboxing and unboxing are helpfull, but use them only if you need it, otherwise prefer primitives.
		 **/
	}
}
