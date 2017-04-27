package com.example.avenue.avenue;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.Socket;



public class MainActivity extends Activity {

    Socket socket;
    OutputStream outputStream;
    PrintStream printStream;
    Button buttonnBC;
    Globals global = Globals.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        global.setData(0);
        Client client = new Client("192.168.43.84",5000,"BC");
        client.execute();
        Toast.makeText(MainActivity.this, "Client Started", Toast.LENGTH_LONG).show();
    }

    public void clickFunction(View view){
        if(view.getId() == R.id.a)
            global.setData(1);

        if(view.getId() == R.id.b)
            global.setData(2);

        if(view.getId() == R.id.c)
            global.setData(3);

        if(view.getId() == R.id.d)
            global.setData(4);
    }
}
