# IRC_Twitch_Chat_Bot

IRC bot for writing one-to-one messages to a chat on Twitch.

To run, clone the repo, and edit IrcLib.py. The settings at the top are important for running your bot. You will have to make a separate account for your bot, and change the value of **NICK** to the bot's name lowercase. **CHAN** is the channel you plan to have the bot arrive in. and **PASS** is a code you can access at www.twitchapps.com/tmi/.

With all of that in place, you will need Python 3 installed. Make sure you have Python 3 runnable by the command line. You can do this on Windows by pressing Windows Key + R, then typing cmd in the popup. Once you have a command line open, type python. An editor should open (looks like this ">>>"). Once there you know python of some kind is successfully installed. To check if you're running Python 3, try "print(5)" and "print 5". The version with the parentheses shoud work in Python 3 and the one without should fail (this is from an older version). 

With all of this in place, you're almost ready to run. Check your settings, and if they all check out, then use "cd" and "dir" from the command line to make your way to the bot's directory. cd moves your current folder to another folder entirely by specifying it's name, and dir lays out the folder you're currently in. (ex. "cd Documents", "dir") Once you arrive in the correct directory, run "python GinyuBot.py". The bot should be running now.

maps.xml contains the one-to-one chat respnses the bot is capable of. Check that file to see what it can do. At the moment the bot responds to "!e1", "!e2", and "!e3". Also the bot has two other functions. "!help" responds with a call for help for whoever wrote it, and "!count" either increments a number count if no number is given after, or sets the count to whatever number is given (ex. "!count", "!count 3").

By editing maps.xml, you can make commands of your very own. Macros like Kappa and PogChamp are available as responses by typing their full name. When the bot posts them the image will show. Have fun!
