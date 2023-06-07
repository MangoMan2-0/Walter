from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)
inst="""hannel:5
Angle:20
Channel:5
Angle:50
Channel:4
Angle:140
Channel:4
Angle:110
Channel:4
Angle:75
Channel:11
Angle:90
Channel:11
Angle:0
Channel:11
Angle:90
Channel:11
Angle:135
Channel:11
Angle:90
Channel:10
Angle:35
Channel:11
Angle:135
Channel:11
Angle:155
Channel:5
Angle:65
Channel:5
Angle:100"""
while True:
    c = int(input("Channel:"))
    a = int(input("Angle:"))
    kit.servo[c].angle=a
def reset():
    kit.servo[5].angle= None#110
    kit.servo[4].angle= None#90
    kit.servo[11].angle= None#150
    kit.servo[12].angle= None
    kit.servo[3].angle= None
    kit.servo[10].angle= None
#sleep(0.1)
#while True:
#    reset()
def walker():
    kit.servo[11].angle=130
    kit.servo[10].angle=160
    sleep(0.025)
    kit.servo[12].angle = 51
    sleep(0.025)
    kit.servo[12].angle = 52
    sleep(0.025)
    kit.servo[12].angle = 53
    sleep(0.025)
    kit.servo[12].angle = 54
    sleep(0.025)
    kit.servo[12].angle = 55
    sleep(0.025)
    kit.servo[12].angle = 56
    sleep(0.025)
    kit.servo[12].angle = 57
    sleep(0.025)
    kit.servo[12].angle = 58
    sleep(0.025)
    kit.servo[12].angle = 59
    sleep(0.025)
    kit.servo[12].angle = 60
    sleep(0.025)
    kit.servo[12].angle = 61
    sleep(0.025)
    kit.servo[12].angle = 62
    sleep(0.025)
    kit.servo[12].angle = 63
    sleep(0.025)
    kit.servo[12].angle = 64
    sleep(0.025)
    kit.servo[12].angle = 65
    sleep(0.025)
    kit.servo[12].angle = 66
    sleep(0.025)
    kit.servo[12].angle = 67
    sleep(0.025)
    kit.servo[12].angle = 68
    sleep(0.025)
    kit.servo[12].angle = 69
    sleep(0.025)
    kit.servo[12].angle = 70
    sleep(0.025)
    kit.servo[12].angle = 71
    sleep(0.025)
    kit.servo[12].angle = 72
    sleep(0.025)
    kit.servo[12].angle = 73
    sleep(0.025)
    kit.servo[12].angle = 74
    sleep(0.025)
    kit.servo[12].angle = 75
    sleep(0.025)
    kit.servo[12].angle = 76
    sleep(0.025)
    kit.servo[12].angle = 77
    sleep(0.025)
    kit.servo[12].angle = 78
    sleep(0.025)
    kit.servo[12].angle = 79
    sleep(0.025)
    kit.servo[12].angle = 80
    sleep(0.025)
    kit.servo[12].angle = 80
    sleep(0.025)
    kit.servo[12].angle = 81
    sleep(0.025)
    kit.servo[12].angle = 82
    sleep(0.025)
    kit.servo[12].angle = 83
    sleep(0.025)
    kit.servo[12].angle = 84
    sleep(0.025)
    kit.servo[12].angle = 85
    sleep(0.5)
    kit.servo[5].angle=75
    kit.servo[4].angle=65
    sleep(1)
    kit.servo[12].angle=80
    sleep(0.025)
    kit.servo[12].angle=79
    sleep(0.025)
    kit.servo[12].angle=78
    sleep(0.025)
    kit.servo[12].angle=77
    sleep(0.025)
    kit.servo[12].angle=76
    sleep(0.025)
    kit.servo[12].angle=75
    sleep(0.025)
    kit.servo[12].angle=74
    sleep(0.025)
    kit.servo[12].angle=73
    sleep(0.025)
    kit.servo[12].angle=72
    sleep(0.025)
    kit.servo[12].angle=71
    sleep(0.025)
    kit.servo[12].angle=70
    sleep(0.025)
    kit.servo[12].angle=70
    sleep(0.025)
    kit.servo[12].angle=69
    sleep(0.025)
    kit.servo[12].angle=68
    sleep(0.025)
    kit.servo[12].angle=67
    sleep(0.025)
    kit.servo[12].angle=66
    sleep(0.025)
    kit.servo[12].angle=65
    sleep(0.025)
    kit.servo[12].angle=64
    sleep(0.025)
    kit.servo[12].angle=63
    sleep(0.025)
    kit.servo[12].angle=62
    sleep(0.025)
    kit.servo[12].angle=61
    sleep(0.025)
    kit.servo[12].angle=60
    kit.servo[12].angle=59
    sleep(0.025)
    kit.servo[12].angle=58
    sleep(0.025)
    kit.servo[12].angle=57
    sleep(0.025)
    kit.servo[12].angle=56
    sleep(0.025)
    #
    
    
    
    
    
    
    
def stand():
    kit.servo[12].angle=70
    sleep(0.1)
    kit.servo[5].angle=10
    sleep(0.1)
    kit.servo[4].angle=10
    sleep(0.1)
    kit.servo[3].angle=130
    sleep(0.1)
    kit.servo[10].angle=150
    sleep(0.1)
    kit.servo[11].angle=145
    sleep(0.1)
def walkr():
    kit.servo[12].angle=60
    sleep(0.1)
    kit.servo[12].angle=63
    sleep(0.1)
    kit.servo[11].angle=100
    sleep(0.025)
    kit.servo[11].angle=110
    sleep(0.025)
    kit.servo[11].angle=120
    sleep(0.025)
    kit.servo[10].angle=180
    
    
    kit.servo[5].angle=35
    sleep(0.1)
    kit.servo[5].angle=45
    sleep(0.1)
    kit.servo[5].angle=55
    sleep(0.1)
    kit.servo[4].angle=75
    kit.servo[12].angle=5
def walkl():
    
    kit.servo[3].angle=141
    sleep(0.025)
    kit.servo[3].angle=142
    sleep(0.025)
    kit.servo[3].angle=143
    sleep(0.025)
    kit.servo[3].angle=144
    sleep(0.025)
    kit.servo[3].angle=145
    sleep(0.025)
    kit.servo[3].angle=146
    sleep(0.025)
    kit.servo[3].angle=147
    sleep(0.025)
    kit.servo[3].angle=148
    sleep(0.025)
    kit.servo[3].angle=149
    sleep(0.025)
    kit.servo[3].angle=150
    sleep(0.025)
    kit.servo[3].angle=151
    sleep(0.025)
    kit.servo[3].angle=152
    sleep(0.025)
    kit.servo[3].angle=153
    sleep(0.025)
    kit.servo[3].angle=154
    sleep(0.025)
    kit.servo[3].angle=155
    sleep(0.025)
    kit.servo[3].angle=156
    sleep(0.025)
    kit.servo[3].angle=157
    sleep(0.025)
    kit.servo[3].angle=158
    sleep(0.025)
    kit.servo[3].angle=159
    sleep(0.025)
    kit.servo[3].angle=160
    #sleep(0.025)
    #kit.servo[3].angle=161
    #sleep(0.025)
    #kit.servo[3].angle=162
    #sleep(0.025)
    #kit.servo[3].angle=163
    #sleep(0.025)
    #kit.servo[3].angle=164
    #sleep(0.025)
    #kit.servo[3].angle=165
    #sleep(0.025)
    #kit.servo[3].angle=166
    #sleep(0.025)
    #kit.servo[3].angle=167
    #sleep(0.025)
    #kit.servo[3].angle=168
    #sleep(0.025)
    #kit.servo[3].angle=169
    #sleep(0.025)
    #kit.servo[3].angle=170
    
    #i = 59
    kit.servo[5].angle=0
    kit.servo[4].angle=10
    kit.servo[11].angle= 90
    kit.servo[10].angle= 90
    kit.servo[3].angle=160
    sleep(0.2)
    kit.servo[3].angle=150
    sleep(0.2)
    kit.servo[3].angle=140
    sleep(0.2)
    kit.servo[12].angle=55
    sleep(0.3)
    #sleep(0.1)
    #kit.servo[5].angle=10
    #sleep(0.1)
    #kit.servo[4].angle=20
    #sleep(0.1)
    #kit.servo[10].angle= 0
    #sleep(0.1)
    #kit.servo[11].angle= 90
    #sleep(1)
    
    
    
    
    
reset()
stand()
sleep(0.5)
while True:
    walker()
    walkl()
    
#12;50
#5;30
#4;40
#3;160
#12;70
#5;90
#while True:
#    kit.servo[11].angle=90
#    kit.servo[10].angle=110
#    kit.servo[9].angle=90
#    kit.servo[5].angle=75
#    kit.servo[4].angle=110
#    kit.servo[3].angle=110
###SQUAT###
#print("begining!")
#kit.servo[11].angle=90
#while True:
#    kit.servo[4].angle=70
#    kit.servo[10].angle=110
#    sleep(1)
#    kit.servo[4].angle=90
#    kit.servo[10].angle=90
#    sleep(1)

###LOG:###
#Channel:4
#Angle:90
#Channel:4
#Angle:70
#Channel:10
#Angle:90
#Channel:10
#Angle:70
#Channel:10
#Angle:120
#Channel:11
#Angle:90
#Channel:10
#Angle:90
#Channel:4
#Angle:90`