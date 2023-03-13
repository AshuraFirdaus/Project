package com.tcpechouts2;

import java.io.*;
import java.net.*;
import java.util.*;

public class EmailClient {
    private static String strHost;
    private static InetAddress host;
    private static final int PORT = 50000;
    private static BufferedReader userEntry;
    private static BufferedReader in;
    private static PrintWriter out;

    public static void main(String args[]) throws IOException {
        userEntry = new BufferedReader(new InputStreamReader(System.in));
        try {
            host = InetAddress.getLocalHost();
            // strHost = args[0] ;
            // host = InetAddress.getByName(strHost);
        } catch (UnknownHostException e) {
            System.out.println("Host ID Not Found");
            System.exit(1);
        }
        run();
    }

    private static void doSend() throws IOException {

        // kirim ke server
        // masukkan message
    }

    private static void doRead() throws IOException {
        // menerima dari server jumlah pesan yang ada di mailbox dalam bentuk string
        // ubah menjadi int
        // lakukan sebanyak jumlah pesan, untuk menerima dari pesan dari server

    }

    private static void run() {
        Socket link = null;
        try {
            link = new Socket(host, PORT);
            in = new BufferedReader(new InputStreamReader(link.getInputStream()));
            out = new PrintWriter(link.getOutputStream(), true);
            String message = "", response = "";
            do {
                String name = "", sendRead = "";
                do {
                    // masukkan name_sendRead misal Andi send
                    // kirim ke server

                    if (!message.equals("close")) {
                        // lakukan pemecahan name=”Andi” sendRead = “send”
                    }
                } while (name.equals("Andi") && name.equals("Budi"));
                if (!message.equals("close")) {
                    if (name.equals("Andi")) {
                        if (sendRead.equals("send")) {
                            doSend();
                        } else if (sendRead.equals("read")) {
                            doRead();
                        }
                    } else if (name.equals("Budi")) {
                        if (sendRead.equals("send")) {
                            doSend();
                        } else if (sendRead.equals("read")) {
                            doRead();
                        }
                    }
                }
            } while (!message.equals("close"));
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                System.out.println("closing connection");
                link.close();
            } catch (IOException e) {
                System.out.println("Unable to disconnect!");
                System.exit(1);
            }
        }
    }
}