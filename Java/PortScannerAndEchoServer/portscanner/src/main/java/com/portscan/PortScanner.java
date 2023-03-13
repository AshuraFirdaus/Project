package com.portscan;

import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class PortScanner {
    public static void main(String[] args) throws UnknownHostException {
        Scanner input = new Scanner(System.in);
        System.out.print("IP Address target: ");
        String host = input.next();
        System.out.print("Scan port from : ");
        int portStarted = input.nextInt();
        System.out.print("until port num : ");
        int portEnded = input.nextInt();
        input.close();
        InetAddress inetAddress = InetAddress.getByName(host);
        System.out.println("inetAddress : " + inetAddress);
        String hostName = inetAddress.getHostName();
        System.out.println("hostName : " + hostName);

        for (int port = portStarted; port <= portEnded; port++){
            try {
                Socket socket = new Socket(hostName, port);
                String text = hostName + " is listening on port" + port;
                System.out.println(text);
                socket.close();
            } catch (Exception e ){
                
            }
            }
        }
}