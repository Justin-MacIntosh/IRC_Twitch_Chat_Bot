import socket
import xml.etree.ElementTree as ET

#--------------------------------------------------Settings---------------------------------------------------
HOST = "irc.twitch.tv"
PORT = 6667
CHAN = "#channel_name"
NICK = "name_of_bot"
PASS = "oauth:hurncowovjkewjwekfneicmwp52n32438"  # www.twitchapps.com/tmi/ will help to retrieve the required authkey
#------------------------------------------------End Settings-------------------------------------------------


#-------------------------------------------------Functions---------------------------------------------------
def send_pong(msg):
    con.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))

def send_message(msg):
    con.send(bytes('PRIVMSG %s :%s\r\n' % (CHAN, msg), 'UTF-8'))

def send_nick(nick):
    con.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))

def send_pass(password):
    con.send(bytes('PASS %s\r\n' % password, 'UTF-8'))

def join_channel(chan):
    con.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))

def part_channel(chan):
    con.send(bytes('PART %s\r\n' % chan, 'UTF-8'))
#------------------------------------------------End Functions--------------------------------------------------


#----------------------------------------------Helper Functions-------------------------------------------------
def get_sender(msg):
    result = ""
    for char in msg:
        if char == "!":
            break
        if char != ":":
            result += char
    return result

def get_message(msg):
    result = ""
    i = 3
    length = len(msg)
    while i < length:
        result += msg[i] + " "
        i += 1
    result = result.lstrip(':')
    return result
#--------------------------------------------End Helper Functions-----------------------------------------------


#----------Socket Initialize----------
con = socket.socket()
con.settimeout(.5)
con.connect((HOST, PORT))
#--------END Socket Initialize--------


#--------------XML Parse--------------
def parse_file(tree):
    inputs = []
    outputs = []
    root = tree.getroot()
    for q in root.findall("map"):
        inputs += [q.find("input").text]
        outputs += [q.find("output").text]
    return [inputs, outputs]
#------------END XML Parse------------
