package com.tcpechouts;

import java.io.*;
import java.net.*;

public class EmailServer {
    private static ServerSocket servSock;
    private static final int PORT = 50000;
    private static final int MAX = 10;
    private static String[] mailbox1 = new String[MAX];
    private static String[] mailbox2 = new String[MAX];
    private static int messageInBox1 = 0;
    private static int messageInBox2 = 0;

    public static void main(String args[]) {
        System.out.println("Opening Port.....\n");
        try {
            servSock = new ServerSocket(PORT);
        } catch (IOException e) {
            System.out.println("Unable to attach to port");
            System.exit(1);
        }
        do {
            run();
        } while (true);
    }

    public static void doSend(String mailbox[], int messageInBox, BufferedReader in, String message)
            throws IOException {

        // tampilkan pesan tersebut di Server
        // menerima pesan dari client yang akan disimpan di mailbox

        if (messageInBox == MAX)
            System.out.println("INBOX FULL");
        else
            mailbox[messageInBox] = message;
    }

    public static void doRead(String mailbox[], int messageInBox, PrintWriter out)
            throws IOException {
        // Tampilkan di server berapa message yang ada di mailbox
        // Jumlah message yang ada di mailbox kirim ke client
        // lakukan perulangan sebanyak jumlah message, selanjutnya tiap message
        // kirim ke client

    }

    private static void run() {
        Socket link = null;
        try {
            link = servSock.accept();
            BufferedReader in = new BufferedReader(new InputStreamReader(link.getInputStream()));
            PrintWriter out = new PrintWriter(link.getOutputStream(), true);
            String message = "", name = "", sendRead = "";
            do {
                if (name.equals("Andi")) {
                    if (sendRead.equals("send")) {
                        System.out.print("Message From Andi : ");
                        doSend(mailbox2, messageInBox2, in, sendRead);
                        if (messageInBox2 < MAX)
                            messageInBox2++;
                    } else if (sendRead.equals("read")) {
                        doRead(mailbox1, messageInBox1, out);
                        messageInBox1 = 0;
                    }
                } else if (name.equals("Budi")) {
                    if (sendRead.equals("send")) {
                        System.out.print("Message From Budi : ");
                        doSend(mailbox1, messageInBox1, in, sendRead);
                        if (messageInBox1 < MAX)
                            messageInBox1++;
                    } else if (sendRead.equals("read")) {
                        doRead(mailbox2, messageInBox2, out);
                        messageInBox2 = 0;
                    }
                }
            } while (!message.equals("close"));
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                System.out.println("*********Closing Connection****");
                link.close();
            } catch (IOException e) {
                System.out.println("Unable to disconnect");
                System.exit(1);
            }
        }
    }
}