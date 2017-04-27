package com.example.avenue.avenue;

import android.os.AsyncTask;
import android.widget.TextView;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.Socket;

/**
 * Created by Anupal Mishra on 27-04-2017.
 */

public class Client extends AsyncTask<Object, Object, Void> {

    String serverAddress;
    int serverPort;
    String response = "";
    Socket socket;

    Globals global = Globals.getInstance();

    Client(String addr, int port, String response) {
        serverAddress = addr;
        serverPort = port;
        this.response = response;
    }

    @Override
    protected Void doInBackground(Object... params) {

        try {
            socket = new Socket(serverAddress, serverPort);
            OutputStream outputStream = socket.getOutputStream();
            PrintStream printStream = new PrintStream(outputStream);
            for(;;) {
                if(global.getData() == 1) {
                    printStream.print("a!");
                    global.setData(0);
                }

                if(global.getData() == 2) {
                    printStream.print("b!");
                    global.setData(0);
                }

                if(global.getData() == 3) {
                    printStream.print("c!");
                    global.setData(0);
                }

                if(global.getData() == 4) {
                    printStream.print("d!");
                    global.setData(0);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }


}

