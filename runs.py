# importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.tools import wait
from pybricks.tools import hub_menu


# setup

BLACK = 5
WHITE = 42
TARGET = 23

hub = PrimeHub()
arm_right = Motor(Port.F)
arm_left = Motor(Port.B)
wheel_right = Motor(Port.D)
wheel_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
back_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.C)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 100)
chassis.use_gyro(True)


# vars
colors = (
    Color.BLACK,
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.NONE,
)
RUN = chassis.straight
speed = chassis.settings
tomer = chassis.curve


def run_1():
    #moving 
    chassis.settings(350)
    chassis.straight(510)
    #catching
    arm_right.run_angle(250, 100, wait=False)
    arm_left.run_angle(250, -100)
    #moving
    chassis.settings(250,100)
    chassis.straight(-310)
    chassis.turn(-113)
    #moving up
    chassis.straight(-280)
    chassis.settings(500,500,300)
    #shrimp
    chassis.straight(160)
    chassis.turn(20)
    chassis.straight(-180)
    chassis.turn(-10)
    chassis.straight(-80)
    chassis.turn(-8)
    chassis.straight(-220)
    chassis.straight(30)
    chassis.straight(-30)
    chassis.straight(280)
    chassis.turn(-30)
    chassis.straight(660)
    #going home
    #chassis.straight(240)
    #chassis.turn(110)
    #chassis.straight(-350)




def run_2():
    #i know it gets kind of stuck while taking dude, dont change IT!
    #settings
     hub.imu.reset_heading(0)
     chassis.settings(straight_acceleration=350)
     chassis.settings(400)
     arm_right.run_time(speed=500,time=1000,wait=False)
     #moving
     chassis.straight(200)
     chassis.turn(45)
     chassis.straight(350)
     chassis.turn(-45)
     chassis.straight(219)
     chassis.turn(-90)
     #pushing coral
     chassis.settings(straight_speed=300,straight_acceleration=200)
     chassis.turn(3)
     chassis.straight(95)
     #taking dude   
     arm_right.run_time(speed=-500,time=2000)
     chassis.straight(-120)
     chassis.turn(34)
     #shark
     chassis.settings(straight_speed=900,straight_acceleration=900)
     chassis.straight(280)
     chassis.settings(straight_speed=400,straight_acceleration=350)
     chassis.straight(-205)
     #moving
     chassis.turn(33)
     chassis.curve(radius=-500,angle=-30)
     chassis.straight(250)
     #puting dude
     chassis.turn(12)
     arm_right.run_time(speed=400,time=1500)
     #pressing 
     RUN(-80)
     RUN(140)
     speed(straight_speed=200,straight_acceleration=200)
     RUN(-78)
     speed(500,500)

    




def run_3():
    #pushing ship
    hub.imu.reset_heading(0)
    arm_right.run_angle(100,100, wait=False)
    arm_left.run_angle(400,-100,wait=False)
    chassis.settings(246,327)
    chassis.straight(-650.42)
    chassis.straight(50.42)
    chassis.straight(-300)
    #pulling crabs
    chassis.settings(50,50)
    chassis.straight(165)
    #moving
    chassis.settings(306.34,301)
    chassis.straight(55)

    chassis.turn(-145)
    chassis.straight(275)
    chassis.turn(-30.8876)
    #pushing ship
    chassis.straight(200)
    chassis.straight(-200)
    chassis.turn(40)
    chassis.straight(-250)
    #moving
    chassis.turn(-70)
    chassis.straight(100)
    chassis.turn(-50)
    chassis.straight(100)
    
    #puting shark
    arm_right.run_angle(-400,100,wait=False)
    chassis.straight(10)
    chassis.straight(-68)

    #going home
    chassis.turn(70)
    chassis.settings(800,800)
    chassis.straight(400, then=Stop.NONE)
    chassis.curve(380,40, then=Stop.NONE)
    chassis.curve(380,-100,)


def run_4():
    
    #shimp 1
    hub.imu.reset_heading(0)
    chassis.settings(600,700)
    chassis.straight(-200)
    chassis.turn(15)
    chassis.straight(-150) 

    #petro
    chassis.straight(200)
    chassis.turn(-13)
    chassis.straight(-250)

    #seaweed
    chassis.straight(110)
    chassis.turn(45)
    chassis.straight(-250)
    chassis.straight(150)

    #shrimp 2
    chassis.settings(200,100)
    chassis.turn(-10)
    chassis.straight(-150)
    chassis.turn(-5)
    chassis.settings(1000,1000)
    chassis.straight(-100)
    chassis.settings(600,700)
    chassis.turn(5)
    chassis.straight(160)

    #shrimp 3
    chassis.turn(25)
    chassis.straight(-150)
    chassis.turn(-5)
    #moving
    chassis.straight(300)
    chassis.turn(160)
    chassis.settings(600,200)
    chassis.straight(380)

    chassis.turn(-15)
    chassis.straight(76.533)
    #pulling rocket
    chassis.turn(-65)
    chassis.straight(-100)
    chassis.straight(230.1)
    arm_right.run_time(-300,2000)
    arm_right.run_time(-300,300)
    chassis.curve(-40,-100)





def run_5():
    hub.imu.reset_heading(0)
    arm_left.run_time(500,500,wait=False)
    #puting seaweed
    speed(700,700)
    RUN(450)
    RUN(-287)
    #moving
    speed(200,200)
    chassis.turn(60)
    speed(300,300)
    RUN(445)
    wheel_left.run_angle(300,170)
    #puting shrimps
    speed(100,100)
    RUN(250)
    arm_left.run_time(-500,1000)
    speed(300,300)


def run_9():
    chassis.curve(-40,-60)



selected = hub_menu("1", "2", "3", "4", "5", "9")
print("gyatt")
print("erez is the best")

if selected == "1":
    run_1()
elif selected == "2":
    run_2()
elif selected == "3":
    run_3()
elif selected == "4":
    run_4()
elif selected == "5":
    run_5()
elif selected == "9":
    run_9()