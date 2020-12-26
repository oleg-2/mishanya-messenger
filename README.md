# mishanya-messenger
Probably the best messenger with double encryption  🔑🔑 and easy 😀 management.

## Take a look at the design
![](https://raw.githubusercontent.com/oleg-2/mishanya-messenger/main/example-chat-scrn.jpg)

## How are messages encrypted?
The main tool is cryptography.fernet. Here we use the following encryption method: message --> (key 1) --> encrypted message 1 --> (key 2) --> encrypted message 2 --> server side database.

## How to install?
First, download the files from this directory on github.
There is a Russian (ru) or English (en) version of the chat.

Now you need free hosting with a domain and php support. Our recommendation: https://www.biz.nf/

For example, we created http://suka.c1.biz/

Using the file manager we need to place 2 files on the hosting in the main directory: data.txt and msg.php. You will find these files in the "server" folder in this github directory.

We have the following: http://suka.c1.biz/data.txt and http://suka.c1.biz/msg.php

Now change the file "server_route.txt" in the folder "client". Specify in it a link to your site, for example, "http://suka.c1.biz/".

Run the file "generate_keys.py" it will create two files "key1.txt" and "key2.txt".

That's it! Chat is set up and ready to use!

Run your chat through the file "mishanya.pyw".

## Tips for use
- to refresh chat messages press F5
- press Enter to send the message or use the "Send" button to do so
- to delete all your correspondence from the server, run the file "delete_server_msg.py"
