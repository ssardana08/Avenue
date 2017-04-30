package com.example.avenue.avenue;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by Anupal Mishra on 30-04-2017.
 */

public class StartActivity extends Activity {
    Button connect;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start);
        connect = (Button)findViewById(R.id.connect);
        final EditText ip = (EditText)findViewById(R.id.ip_address);

        connect.setOnClickListener(new View.OnClickListener()
        {    public void onClick(View v)
        {
            String msg = ip.getText().toString();
            Intent intent = new Intent(getBaseContext(), MainActivity.class);
            intent.putExtra("ip", msg);
            startActivity(intent);
            finish();
        }
        });
    }
}
