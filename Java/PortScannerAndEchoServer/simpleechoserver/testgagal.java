package com.simpleechoserver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class simpleechoserver{
    private static ServerSocket servSock;
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Input Port Server Yang Diinginkan");
        int PORT = input.nextInt();
        input.close();
        try {
            servSock = new ServerSocket(PORT);
            InetAddress host = InetAddress.getLocalHost();
            System.out.println("SimplEechoServer is on at " + host + "with port" + PORT);
            while(true){
                Socket incoming = servSock.accept();
                BufferedReader in = new BufferedReader(new InputStreamReader(incoming.getInputStream()));
                PrintWriter out = new PrintWriter(incoming.getOutputStream(), true);
                out.println("Hello this is from the java Simpleechoserver");
                out.println("Enter to BYE to exit ");
                out.flush();
                while (true){
                    String str = in.readLine();
                    out.println("Echo: " + str);
                    out.flush();
                    if (str.trim().equals("BYE")){
                        break;
                    }
                    in.close();
                    out.close();
                    incoming.close();
                }
            }
        }catch(Exception e){
                System.out.println("Unable to attach to port or problem disconnected");
                System.exit(1);
            }
    }
} 
