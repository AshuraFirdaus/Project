package com.targetname;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;
/**
* Network Programming IpFinder - Menemukan IP address
*
*/
public class App {
		public static void main(String[] args) {
		String host;
		Scanner input = new Scanner(System.in);
		System.out.println("Input nama host: , misal www.google.com");
		System.out.println("Input nama host: ");
		host = input.next();
		try {
		InetAddress address = InetAddress.getByName(host);
		System.out.println("IP address: " + address.toString());
		} catch (UnknownHostException e) {
		System.out.println("Tidak bisa mendapatkan " + host + " atau jaringan terputus");
	}
	 input.close();
    }
}
