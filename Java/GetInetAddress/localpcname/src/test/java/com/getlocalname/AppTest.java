package com.getlocalname;

import static org.junit.Assert.assertTrue;

import java.net.InetAddress;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );
    }

    public static void main(String[] args) throws Exception {
     InetAddress host = null;
     host = InetAddress.getLocalHost();
     System.out.println("Nama komputer Anda :" + host.getHostName());
     System.out.println("identitas komputer lengkap : " + host);
     }
}
