import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
from termcolor import colored
import smtplib
import base64
#GPIO.RPI_REVISION

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO_1 = 12 #Fan at BCM Pin @ GPIO12
GPIO_2 = 5 #Blue LED at BCM Pin @ GPIO16
GPIO_3 = 26 #Yellow LED at BCM Pin @ GPIO26
GPIO_4 = 19
GPIO.setup(GPIO_4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_1, GPIO.OUT)
GPIO.setup(GPIO_2, GPIO.OUT)
GPIO.setup(GPIO_3, GPIO.OUT)

GPIO.output(GPIO_2,0)

pw = base64.b64decode("Zm9yUHl0aG9u")

def send_mail(subject):

        try:
                    fromaddr = 'skyseeearth@gmail.com'
                    toaddrs  = 'akashkumar03@gmail.com'
                    SUBJECT = subject
                    TEXT = ''
                    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                    # Credentials (if needed)
                    username = 'skyseeearth@gmail.com'
                    password = pw
                    # The actual mail send
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
        except:
                pass


filename1 = '/media/tp_nas/drowsyness/eye.txt' #Win NAS drive where file resides
filename2 = '/media/tp_nas/eyebrows/eye.txt' #Win NAS drive where file resides
#file = open(filename,'r')

on_eyes = None
off_eyes = None
response_eyes  = 0
i_eyes = 0

while 1:
       try:
      	  response_eyes  = int(os.popen("cat "+ filename1 + " 2>/dev/null").read())
	  #response_brows = int(os.popen("cat "+ filename2 + " 2>/dev/null").read())
       except:
	    #response = 0
	    #print("Gotcha!!!")
	     pass
       #print response_eyes
       if response_eyes  == 1:
			  #off_eyes = None
		   	  #if on_eyes == None:
				       i_eyes += 1
				       print colored(("EYE BLUEE FAN On  @ " + str(datetime.now().strftime('%H:%M')) + " & COUNT " + str(i_eyes)), 'blue')
 			               #GPIO.output(GPIO_1,1)
                 		       GPIO.output(GPIO_2,1)
				       #on_eyes = True
				      
				       try:
			   		  os.system("rm " + filename1 + " 2>/dev/null")
       				       except:
                                             pass
				       time.sleep(5)
				       send_mail('Driver Took Nap')
				       GPIO.output(GPIO_2,0)
				       response_eyes  = 0
				       #off_eyes = None
                          	       #if on_eyes == None:
				       send_mail('ALERT!!! Driver DROWSED @ ' + str(datetime.now().strftime("%H:%M on %b-%d-%y")))
						#	  on_eyes = True
       #else:
	    #on_eyes = None
	    #if off_eyes == None:
			#on_eyes = None
			#off_eyes = True
	#   response_eyes  = 0
       #print "check"
       time.sleep(.5)

