package com.uts2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author : aryo.nurutomo
 */
public class EmailClient {
    private static String strHost;
    private static InetAddress host;
    private static final int PORT = 5000;
    private static BufferedReader userEntry;
    private static BufferedReader in;
    private static PrintWriter out;

    public static void main(String[] args) {
        userEntry = new BufferedReader(new InputStreamReader(System.in));
        try {
            host = InetAddress.getLocalHost();
            // strHost = args[0];
            // host = InetAddress.getByName(strHost);
        } catch (UnknownHostException e) {
            System.out.println("Host ID Not Found");
            System.exit(1);
        }
        run();
    }

    private static void doSend() throws IOException {
        // masukkan message
        System.out.println("Enter 1‐line message");
        String message = userEntry.readLine();
        // kirim ke server
        out.println(message);
    }

    private static void doRead() throws IOException {
        // menerima dari server jumlah pesan yang ada di mailbox dalam bentuk string
        // ubah menjadi int
        // lakukan sebanyak jumlah pesan, untuk menerima dari pesan dari server
        String allMessage = new String();
        allMessage = in.readLine();
        StringTokenizer st = new StringTokenizer(allMessage, "|");
        System.out.println("Jumlah Pesan = " + st.countTokens());
        int countMessage = 1;
        while (st.hasMoreTokens()) {
            System.out.println(countMessage + " : " + st.nextToken());
            countMessage++;
        }
    }

    private static void run() {
        Socket link = null;
        try {
            link = new Socket(host, PORT);
            in = new BufferedReader(new InputStreamReader(link.getInputStream()));
            out = new PrintWriter(link.getOutputStream(), true);
            String message = new String();
            do {
                String name = "", sendRead = "";
                do {
                    // masukkan name_sendRead misal Andi send
                    // kirim ke server
                    System.out.print("Enter [name] send or read : ");
                    message = userEntry.readLine();
                    out.println(message);
                    if (!message.equals("close")) {
                        // lakukan pemecahan name = 'Andi' sendRead = 'send'
                        StringTokenizer tokenizer = new StringTokenizer(message);
                        List<String> tokens = new ArrayList<>();
                        while (tokenizer.hasMoreTokens()) {
                            tokens.add(tokenizer.nextToken());
                        }
                        name = tokens.get(0);
                        sendRead = tokens.get(1);
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
            throw new RuntimeException(e);
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