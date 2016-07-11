#!/usr/bin/env python3

# GinyuBot.py - A Simple IRC-bot Written in Python

import re
import time
import sys
import operator
import xml.etree.ElementTree as ET

from IrcLib import *

#Handles any message in the chat, and returns the question number we're on.
#If the answer
def handle_message(msg, sender, inputs, outputs):
    #If the lenth isn't 0
    if len(msg) >= 1:
        msg = msg.split()

        for i in range(len(inputs)):
            if (msg[0] == inputs[i]):
                send_message(outputs[i])
                return

        if (msg[0] == "!help"):
            send_message("Help " + sender)
            return
        elif (msg[0] == "!count"):
            with open("count.txt", "r+") as f:
                data = f.read()
                count = int(data)
                f.seek(0)
                if (len(msg) > 1):
                    if(msg[1].isdigit()):
                        f.write(str(msg[1]))
                        send_message("COUNT: " + str(int(msg[1])))
                    else:
                        f.write(data)
                        send_message("THAT'S NOT A NUMBER")
                else:
                    f.write(str(count + 1))
                    send_message("COUNT: " + str(count+1))
                f.truncate()
                f.close()
            return
    return

#------------------------------------------------------------------------------------------------------------------------------------------

#Beginning of Actual Script

#Standard IRC initialization
send_pass(PASS)
send_nick(NICK)
join_channel(CHAN)

#XML Parse
tree = ET.parse('maps.xml')
parsed = parse_file(tree)
inputs = parsed[0]
outputs = parsed[1]

data = ""

#Main Listening Loop
while True:
    try:
        #---------Receive Data---------
        data = data+con.recv(1024).decode('UTF-8')
        data_split = re.split(r"[~\r\n]+", data)
        data = data_split.pop()
        #-------END Receive Data-------

        for line in data_split:
            line = str.rstrip(line)
            split_line = str.split(line)

            if len(split_line) >= 1:
                if split_line[0] == 'PING':
                    send_pong(split_line[1])
                if split_line[1] == 'PRIVMSG':
                    #-------Parse Msg-------
                    sender = get_sender(line)
                    message = get_message(split_line)

                    print(str(sender) + ' - \"' + str(message.strip()) + "\"")

                    handle_message(message, sender, inputs, outputs)
                    #-----END Parse Msg-----
            time.sleep(.1)
    except socket.timeout or socket.error:
        continue
