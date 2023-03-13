package com.getlocalname;

import java.net.InetAddress;
/**
* GetNameComputer program untuk mengetahui nama komputer lokal
*
*/
public class GetNameComputer {
    public static void main(String[] args) throws Exception {
        InetAddress host = null;
        host = InetAddress.getLocalHost();
        System.out.println("Nama Komputer Anda :" + host.getHostName());
        System.out.println("identitas Komputer Lengkap : " + host);
    }
}