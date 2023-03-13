package com.uts1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author : aryo.nurutomo
 */
public class EmailServer {
    private static ServerSocket servSock;
    private static final int PORT = 5000;
    private static final int MAX = 10;
    private static String[] mailbox1 = new String[MAX]; // punya Andi
    private static String[] mailbox2 = new String[MAX]; // punya Budi
    private static int messageInBox1 = 0; // punya Andi
    private static int messageInBox2 = 0; // punya Budi

    public static void main(String[] args) {
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

    public static void doSend(String mailbox[], int messageInBox, BufferedReader in) throws IOException {
        // menerima pesan dari client yang akan disimpan di mailbox
        String message = in.readLine();
        // tampilkan pesan tersebut di Server
        System.out.println(message);
        if (messageInBox == MAX) {
            System.out.println("INBOX FULL");
        } else {
            mailbox[messageInBox] = message;
        }
    }

    public static void doRead(String mailbox[], int messageInBox, PrintWriter out) {
        // Tampilkan di server berapa message yang ada di mailbox
        System.out.println("Message InBox : " + messageInBox);
        // Jumlah message yang ada di mailbox kirim ke client
        // lakukan perulangan sebanyak jumlah message, selanjutnya tiap message kirim ke
        // client
        String allMessage = new String();
        for (int i = 0; i < messageInBox; i++) {
            allMessage = allMessage + mailbox[i] + "|";
        }
        out.println(allMessage);
    }

    private static void run() {
        Socket link = null;
        try {
            link = servSock.accept();
            BufferedReader in = new BufferedReader(new InputStreamReader(link.getInputStream()));
            PrintWriter out = new PrintWriter(link.getOutputStream(), true);
            String message = "", name = "", sendRead = "";
            do {
                // menerima pesan dari client berupa name dan sendRead (Andi read)
                message = in.readLine();
                // lakukan pemecahan String dg menggunakan StringTokenizer simpan
                StringTokenizer tokenizer = new StringTokenizer(message);
                List<String> tokens = new ArrayList<>();
                while (tokenizer.hasMoreTokens()) {
                    tokens.add(tokenizer.nextToken());
                }
                name = tokens.get(0);
                sendRead = tokens.get(1);
                // name:Andi or Budi, sendRead = send or read
                if (name.equals("Andi")) {
                    if (sendRead.equals("send")) {
                        System.out.print("Message From Andi : ");
                        doSend(mailbox2, messageInBox2, in);
                        if (messageInBox2 < MAX) {
                            messageInBox2++;
                        }
                    } else if (sendRead.equals("read")) {
                        doRead(mailbox1, messageInBox1, out);
                        messageInBox1 = 0;
                    }
                } else if (name.equals("Budi")) {
                    if (sendRead.equals("send")) {
                        System.out.print("Message From Budi : ");
                        doSend(mailbox1, messageInBox1, in);
                        if (messageInBox1 < MAX) {
                            messageInBox1++;
                        }
                    } else if (sendRead.equals("read")) {
                        doRead(mailbox2, messageInBox2, out);
                        messageInBox2 = 0;
                    }
                }
            } while (!message.equals("close"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                System.out.println("*******Closing Connection*******");
                link.close();
            } catch (IOException e) {
                System.out.println("Unable to disconnect");
                System.exit(1);
            }
        }
    }
}
