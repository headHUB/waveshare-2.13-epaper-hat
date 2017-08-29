import time
import spidev as SPI
import EPD_driver
import datetime
import subprocess


EPD2X9 = 0
EPD02X13 = 1
EPD1X54 = 0

bus = 0 
device = 0
 	
disp = EPD_driver.EPD_driver(spi=SPI.SpiDev(bus, device))

# stats are gathered at the top because you dont have to wait for the screen to refresh to find out your code sucks
print '---- start gathereing some stats -------'

  # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
cmd = "w |head -n1|awk '{print $6,$8,$2,$3}'"
CPU = subprocess.check_output(cmd, shell = True )
cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell = True )
cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
Disk = subprocess.check_output(cmd, shell = True )
# OLD weather cmd = "curl -s wttr.in/?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g'"
# old, cleaned it up a lot. cmd = "curl -s wttr.in/?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g' | tr -s ' '"
cmd = "curl -s wttr.in/?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g' | tr -s ' ' |awk '{print $1,$2,$3,$4$5,$7}'"
Weather = subprocess.check_output(cmd, shell = True )
cmd = "date|cut -c-26"
Date = subprocess.check_output(cmd, shell = True)
    
    
#print str(Weather)    this was just here to check the format of the weather, 

##### so, if you dont do the full clear it works fine! but gets a touch ghosty
####### if you remove the Dis_Clear_part(), everything stops working #quality 
#init and Clear full screen
#print '------------init and Clear full screen------------'
#disp.Dis_Clear_full()
#init and Clear part screen  
#print '------------init and Clear part screen------------'
disp.Dis_Clear_part()
######dont remove the above clears!!! 

#String Font size range seems to be from 12 to 16.. for some reason
#going bottom to top, because im lazy
print '------------Show string------------'
disp.Dis_String(0, 1, str(Date),16)
disp.Dis_String(0, 20, "Current weather:",16)
disp.Dis_String(0, 35, str(Weather),16)
disp.Dis_String(0, 102, str(CPU) + " " + str(Disk),12)
disp.Dis_String(0, 114, "IP:" + str(IP) + " " + str(MemUsage),12) 

#time.sleep(DELAYTIME)

#print '------------show time------------'
#while 1 :
#	now = datetime.datetime.now()
#	now_sec = now.second%10
#	next_sec = 11  #Guaranteed next greater than 9
#	if now_sec != next_sec:
#		disp.Dis_showtime(now.hour,now.minute,now.second)
#		next_sec = now.second%10
