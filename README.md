# SIS Bot v4 #
### (updated from nkrishn9's and yzhan289's SIS Bots)  ###

This selenium bot allows you to register for classes on the Johns Hopkins SIS portal right at 7:00 AM, virtually guaranteeing a spot in all of your classes.

### WARNING: This has only been tested on Mac OS (and will probably only work on it). ###

## Setup Instructions ##
First, make sure all of the classes you want to register for are in your cart on SIS.

```
git clone https://github.com/bwong19/SIS-Bot.git
cd SIS-Bot
pip install selenium
brew cask install chromedriver
```

SIS uses the naval observatory clock to determine time. Therefore, your system must be synced to this clock to ensure the bot does not click too early or too late. On Mac OS, it is really easy to change your default.

1. Navigate to System Preferences and click Date and Time.
2. Click the lock on the bottom left of your window and enter your password.
3. Change "Apple Americas/U.S. (time.apple.com.)" to "tick.usno.navy.mil"
4. Click the lock again to save your changes.

![time instructions](https://github.com/bwong19/SIS-Bot/blob/master/time_instruct.png "Logo Title Text 1")


## Running Instructions ##
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes.
```
python bot.py SIS_Username SIS_Password
```
