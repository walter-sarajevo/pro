#encoding = utf-8

tcpic = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x07,0xc0,0x00,0x00,0x00,0x00,0x00,0x00,
         0x03,0xf0,0x00,0x00,0x00,0x00,0x00,0x00,
         0x03,0xfc,0x00,0x00,0x00,0x00,0x00,0x00,
         0x03,0xff,0x00,0x00,0x00,0x00,0x00,0x00,
         0x01,0xff,0xc0,0x00,0x00,0x00,0x00,0x00,
         0x01,0xff,0xf0,0x00,0x00,0x00,0x00,0x00,
         0x01,0xff,0xfc,0x00,0x00,0x00,0x00,0x00,
         0x00,0xff,0xff,0x00,0x00,0x00,0x00,0x00,
         0x00,0xff,0xff,0x80,0x00,0x00,0x00,0x00,
         0x00,0x7f,0xff,0xe0,0x00,0x00,0x00,0x00,
         0x00,0x7f,0xff,0xf8,0x00,0x00,0x00,0x00,
         0x00,0x7f,0xff,0xfe,0x00,0x00,0x00,0x00,
         0x00,0x0f,0xff,0xff,0x00,0x00,0x00,0x00,
         0x00,0x00,0xff,0xff,0x80,0x00,0x00,0x00,
         0x00,0x1f,0x1f,0xff,0xe0,0x00,0x00,0x00,
         0x00,0x1f,0xe1,0xff,0xf0,0x00,0x00,0x00,
         0x00,0x1f,0xfe,0x3f,0xfc,0x00,0x00,0x00,
         0x00,0x0f,0xff,0xc7,0xfe,0x00,0x00,0x00,
         0x00,0x0f,0xff,0xf0,0xff,0x00,0x00,0x00,
         0x00,0x0f,0xff,0xfe,0x3f,0xc0,0x00,0x00,
         0x00,0x07,0xff,0xff,0xc7,0xe0,0x00,0x00,
         0x00,0x03,0xff,0xff,0xf9,0xf8,0x00,0x00,
         0x00,0x03,0xff,0xff,0xfe,0x7c,0x00,0x00,
         0x00,0x01,0xff,0xff,0xff,0x9e,0x00,0x00,
         0x00,0x01,0xff,0xff,0xff,0xe7,0x00,0x00,
         0x00,0x00,0xff,0xff,0xff,0xf9,0x80,0x00,
         0x00,0x00,0xff,0xff,0xff,0xfe,0x00,0x00,
         0x00,0x00,0x07,0xff,0xff,0xff,0x80,0x00,
         0x00,0x00,0x00,0x01,0xff,0xff,0xe0,0x00,
         0x00,0x00,0x3f,0xe0,0x01,0xff,0xf8,0x00,
         0x00,0x00,0x3f,0xff,0xfe,0x03,0xf4,0x00,
         0x00,0x00,0x3f,0xff,0xff,0xfc,0x00,0x00,
         0x00,0x00,0x1f,0xff,0xff,0xff,0xfc,0x00,
         0x00,0x00,0x0f,0xff,0xff,0xff,0xfc,0x00,
         0x00,0x00,0x0f,0xff,0xff,0xff,0xc1,0x80,
         0x00,0x00,0x07,0xff,0xff,0xf8,0x3f,0x00,
         0x00,0x00,0x03,0xff,0xff,0xc7,0xfe,0x00,
         0x00,0x00,0x03,0xff,0xfc,0x3f,0xfc,0x00,
         0x00,0x00,0x01,0xff,0xe1,0xff,0xf0,0x00,
         0x00,0x00,0x00,0xff,0x8f,0xff,0xe0,0x00,
         0x00,0x00,0x00,0x7c,0x7f,0xff,0xc0,0x00,
         0x00,0x00,0x00,0x71,0xff,0xff,0x80,0x00,
         0x00,0x00,0x00,0x07,0xff,0xff,0x80,0x00,
         0x00,0x00,0x00,0x1f,0xff,0xff,0x00,0x00,
         0x00,0x00,0x00,0x7f,0xff,0xfe,0x00,0x00,
         0x00,0x00,0x01,0xff,0xff,0xfe,0x00,0x00,
         0x00,0x00,0x03,0xff,0xff,0xfc,0x00,0x00,
         0x00,0x00,0x0f,0xff,0xff,0xf8,0x00,0x00,
         0x00,0x00,0x1f,0xff,0xff,0xf8,0x00,0x00,
         0x00,0x00,0x7f,0xff,0xff,0xf8,0x00,0x00,
         0x00,0x00,0xff,0xff,0xff,0xf0,0x00,0x00,
         0x00,0x03,0xff,0xff,0xff,0xf0,0x00,0x00,
         0x00,0x07,0xff,0xff,0xff,0xe0,0x00,0x00,
         0x00,0x0f,0xff,0xff,0xff,0xe0,0x00,0x00,
         0x00,0x3f,0xff,0xff,0xff,0xe0,0x00,0x00,
         0x00,0x7f,0xff,0xff,0xff,0xe0,0x00,0x00,
         0x00,0xff,0xff,0xff,0xff,0xc0,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

tcpic_op = [0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xf8,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xf8,0x3f,0xff,0xff,0xff,0xff,0xff,0xff,
0xfc,0x0f,0xff,0xff,0xff,0xff,0xff,0xff,
0xfc,0x03,0xff,0xff,0xff,0xff,0xff,0xff,
0xfc,0x00,0xff,0xff,0xff,0xff,0xff,0xff,
0xfe,0x00,0x3f,0xff,0xff,0xff,0xff,0xff,
0xfe,0x00,0x0f,0xff,0xff,0xff,0xff,0xff,
0xfe,0x00,0x03,0xff,0xff,0xff,0xff,0xff,
0xff,0x00,0x00,0xff,0xff,0xff,0xff,0xff,
0xff,0x00,0x00,0x7f,0xff,0xff,0xff,0xff,
0xff,0x80,0x00,0x1f,0xff,0xff,0xff,0xff,
0xff,0x80,0x00,0x07,0xff,0xff,0xff,0xff,
0xff,0x80,0x00,0x01,0xff,0xff,0xff,0xff,
0xff,0xf0,0x00,0x00,0xff,0xff,0xff,0xff,
0xff,0xff,0x00,0x00,0x7f,0xff,0xff,0xff,
0xff,0xe0,0xe0,0x00,0x1f,0xff,0xff,0xff,
0xff,0xe0,0x1e,0x00,0x0f,0xff,0xff,0xff,
0xff,0xe0,0x01,0xc0,0x03,0xff,0xff,0xff,
0xff,0xf0,0x00,0x38,0x01,0xff,0xff,0xff,
0xff,0xf0,0x00,0x0f,0x00,0xff,0xff,0xff,
0xff,0xf0,0x00,0x01,0xc0,0x3f,0xff,0xff,
0xff,0xf8,0x00,0x00,0x38,0x1f,0xff,0xff,
0xff,0xfc,0x00,0x00,0x06,0x07,0xff,0xff,
0xff,0xfc,0x00,0x00,0x01,0x83,0xff,0xff,
0xff,0xfe,0x00,0x00,0x00,0x61,0xff,0xff,
0xff,0xfe,0x00,0x00,0x00,0x18,0xff,0xff,
0xff,0xff,0x00,0x00,0x00,0x06,0x7f,0xff,
0xff,0xff,0x00,0x00,0x00,0x01,0xff,0xff,
0xff,0xff,0xf8,0x00,0x00,0x00,0x7f,0xff,
0xff,0xff,0xff,0xfe,0x00,0x00,0x1f,0xff,
0xff,0xff,0xc0,0x1f,0xfe,0x00,0x07,0xff,
0xff,0xff,0xc0,0x00,0x01,0xfc,0x0b,0xff,
0xff,0xff,0xc0,0x00,0x00,0x03,0xff,0xff,
0xff,0xff,0xe0,0x00,0x00,0x00,0x03,0xff,
0xff,0xff,0xf0,0x00,0x00,0x00,0x03,0xff,
0xff,0xff,0xf0,0x00,0x00,0x00,0x3e,0x7f,
0xff,0xff,0xf8,0x00,0x00,0x07,0xc0,0xff,
0xff,0xff,0xfc,0x00,0x00,0x38,0x01,0xff,
0xff,0xff,0xfc,0x00,0x03,0xc0,0x03,0xff,
0xff,0xff,0xfe,0x00,0x1e,0x00,0x0f,0xff,
0xff,0xff,0xff,0x00,0x70,0x00,0x1f,0xff,
0xff,0xff,0xff,0x83,0x80,0x00,0x3f,0xff,
0xff,0xff,0xff,0x8e,0x00,0x00,0x7f,0xff,
0xff,0xff,0xff,0xf8,0x00,0x00,0x7f,0xff,
0xff,0xff,0xff,0xe0,0x00,0x00,0xff,0xff,
0xff,0xff,0xff,0x80,0x00,0x01,0xff,0xff,
0xff,0xff,0xfe,0x00,0x00,0x01,0xff,0xff,
0xff,0xff,0xfc,0x00,0x00,0x03,0xff,0xff,
0xff,0xff,0xf0,0x00,0x00,0x07,0xff,0xff,
0xff,0xff,0xe0,0x00,0x00,0x07,0xff,0xff,
0xff,0xff,0x80,0x00,0x00,0x07,0xff,0xff,
0xff,0xff,0x00,0x00,0x00,0x0f,0xff,0xff,
0xff,0xfc,0x00,0x00,0x00,0x0f,0xff,0xff,
0xff,0xf8,0x00,0x00,0x00,0x1f,0xff,0xff,
0xff,0xf0,0x00,0x00,0x00,0x1f,0xff,0xff,
0xff,0xc0,0x00,0x00,0x00,0x1f,0xff,0xff,
0xff,0x80,0x00,0x00,0x00,0x1f,0xff,0xff,
0xff,0x00,0x00,0x00,0x00,0x3f,0xff,0xff,
0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,
0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff]