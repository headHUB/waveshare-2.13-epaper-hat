# waveshare-2.13-epaper-hat
E-paper RaspberryPi beside clock project with weather. 

So I cheaped out and bought the waveshare 2.13" epaper / eink hat for the RaspberryPi, the kind thats $20 on ebay and 250x122 2.13 inch 

This was not a great idea and the screen is almost as immiture as I am and its a pain to get working, 

I have uploaded my code incase someone else has bought this screen and needs help, its not good code but it should point you in the right direction.
This is by no means finished, but it is (currently) working as a clock and bedside weather info.(most of the time) 

To install and setup the drivers, follow the guide on the wave share wiki.
This is a work in progress, below is my notes.

---

## To Do list: 
#### Learn to program.
#### Fix the random the "i"'s that appear after lines. (cut?)
#### Scrap the script for one that builds a png in imagemagik and uploads it, found a script for this, but images dont display right.
#### Not scrape a public site for their weather..  or Cache weather as i really dont need to pull that every hour. 
#### double diget vs single diget temps screw up the awk's :( 
#### Streemline the weather pull, itemize it. 

---

## Done list: 
#### Crontab to update every minute: * * * * * /usr/bin/python /home/pi/clock/stats.py >/dev/null 2>&1
#### Turn off built in LED: "sudo echo 1 | sudo tee /sys/class/leds/led0/brightness", Credit > https://www.jeffgeerling.com/blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi 
#### Rearange items and change the size of the text. 

---

## Known issues:
#### Cant seem to choose a bigger size of text other than "16" could get around this by building some kind of assci art. 

---
