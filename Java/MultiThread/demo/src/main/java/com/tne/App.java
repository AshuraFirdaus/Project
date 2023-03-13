package com.tne;


class PrintNameThread extends Thread {
    PrintNameThread(String name) {
        super(name);
        start();
    }

    public void run() {
        String name = getName();
        for (int i = 0; i < 100; i++){
            System.out.print(name);
        }
    }
}
class TestThread {
    public static void main(String args[]){
        PrintNameThread pnt1 =
            new PrintNameThread("A");
        PrintNameThread pnt2 =
            new PrintNameThread("B");
        PrintNameThread pnt3 =
            new PrintNameThread("C");
        PrintNameThread pnt4 =
            new PrintNameThread("D");
    }
}
class TestThread2 {
    public static void main(String args[]){
        new PrintNameThread("A");
        new PrintNameThread("B");
        new PrintNameThread("C");
        new PrintNameThread("D");
    }
}

