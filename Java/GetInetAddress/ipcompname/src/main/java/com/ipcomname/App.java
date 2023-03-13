package com.ipcomname;

import java.net.InetAddress;
import java.util.Scanner;

class IPtoName {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Input IP Address lokal ataupun komputer di jaringan");
        System.out.println("IP Address : ");
        String host = input.next();
        input.close();
        InetAddress address = null;
        try {
            address = InetAddress.getByName(host);
        } catch (Exception e){
            System.out.println("invalid IP");
            System.exit(0);
        }
        System.out.println(address.getHostName());
    }
}