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
gay_or_tomer_YOU_CAN_CALL_IT_WHAT_EVER_YOU_WANT_IT_ACTUALLY_DOSE_NOT_MATTAR_AT_ALL = chassis.curve


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
<<<<<<< HEAD
    #i know it gets kind of stuck while taking dude, dont change IT!
    #settings
=======

>>>>>>> 029199e429b5002ae0d92def10f1273b02788128
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
     chassis.turn(-87)
     #pushing coral
     chassis.settings(straight_speed=300,straight_acceleration=200)
     chassis.turn(3)
     chassis.straight(90)
     #taking dude   
     arm_right.run_time(speed=-500,time=2000)
     chassis.straight(-120)
     chassis.turn(34)
     #shark
     chassis.settings(straight_speed=900,straight_acceleration=900)
     chassis.straight(280)
     chassis.settings(straight_speed=400,straight_acceleration=350)
<<<<<<< HEAD
     chassis.straight(-205)
=======
     chassis.straight(-200)
>>>>>>> 029199e429b5002ae0d92def10f1273b02788128
     #moving
     chassis.turn(33)
     chassis.curve(radius=-500,angle=-30)
    
     chassis.straight(250)
<<<<<<< HEAD
     #puting dude
     chassis.turn(12)
     arm_right.run_time(speed=400,time=1500)
     #pressing 
     RUN(-80)
     RUN(140)
     speed(straight_speed=200,straight_acceleration=200)
     RUN(-78)
     speed(500,500)

=======
     chassis.turn(5)
     arm_right.run_time(speed=400,time=1500)
    #  chassis.settings(straight_speed=600,straight_acceleration=700)
    #  #puting dude
    #  arm_right.run_angle(speed=-400,rotation_angle=-30)
    #  chassis.straight(15)
    #  wheel_right.run_angle(speed=300,rotation_angle=30)
    #  chassis.straight(-15)
    #  arm_right.run_angle(speed=-400,rotation_angle=-600)
    # #  wheel_right.run_angle(300,30)
    #  #geting home 
    #  chassis.straight(-300)
    #  chassis.settings(straight_speed=600,straight_acceleration=500)
    #  chassis.curve(radius=-500,angle=-90)
    #  print("erez is the best shubi dubi")
>>>>>>> 029199e429b5002ae0d92def10f1273b02788128
    




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
    chassis.turn(50)
    chassis.straight(-250)
    chassis.straight(150)

    #shrimp 2
    chassis.settings(200,100)
    chassis.turn(-15)
    chassis.straight(-150)
    chassis.turn(-5)
    chassis.settings(1000,1000)
    chassis.straight(-100)
    chassis.settings(600,700)
    chassis.turn(5)
    chassis.straight(160)

    #shrimp 3
    chassis.turn(25)
<<<<<<< HEAD
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


=======
    chassis.settings(700,1000)
    chassis.straight(-170)
    # chassis.curve()
    # chassis.turn(60)
    # gay(200)
    # # chassis.settings(150,100)
    # chassis.straight(-100)
    # chassis.turn(-10)
    # chassis.straight(-140,wait=False)
    # wait(750)
    # chassis.straight(170)
    # chassis.turn(60)
    # chassis.straight(60)
    # chassis.turn(30)
    # chassis.straight(150)
    # chassis.turn(50)
    # chassis.straight(140)
    # chassis.turn(-60)
    # arm_right.run_time(-300,2000)
    # arm_right.run_time(300,1000,wait=False)
    # wait(0)
    # chassis.straight(-300)
    # chassis.straight(80)
    # chassis.turn(30)
    # chassis.straight(160)
    # chassis.turn(-30)
    # chassis.turn(60)
    # chassis.straight(160)
    # chassis.straight(200)
    # chassis.turn(50)
    # chassis.settings(200)
    # chassis.straight(-120)
    # # chassis.straight(100)
    # chassis.settings(1000)
    # chassis.curve(100,50)
    # chassis.turn(45)
    # chassis.straight(260)
    # chassis.turn(-55)
    # chassis.straight(75)
    # arm_right.run_time(-300,2000)
    # chassis.turn(60)
    # chassis.straight(-1000)
>>>>>>> 029199e429b5002ae0d92def10f1273b02788128



def run_5():
   chassis.settings(400,400) 
   chassis.straight(400)
   chassis.straight(-300)
   chassis.turn(50)
   chassis.straight(500)
   chassis.turn(62)
   chassis.straight(420)
   arm_left.run_angle(500,-70)
   


def run_9():
<<<<<<< HEAD
    chassis.curve(-40,-60)

=======
    chassis.settings(1000,1000)
    chassis.straight(-100000)
>>>>>>> 029199e429b5002ae0d92def10f1273b02788128


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