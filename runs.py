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



def run_1():
     #moving 
    chassis.settings(350)
    chassis.straight(510)
    #catching
    arm_right.run_angle(250, 120, wait=False)
    arm_left.run_angle(250, -120)
    #moving
    chassis.settings(250,100)
    chassis.straight(-270)
    chassis.turn(-113)
    #moving up
    chassis.straight(-300)
    chassis.settings(500,500,300)
    #going home
    chassis.straight(240)
    chassis.turn(110)
    chassis.straight(-350)




def run_2():

     hub.imu.reset_heading(0)
     chassis.settings(251.7,567.8)
     chassis.settings(403.0032)
     #moving
     chassis.straight(200.0908)
     chassis.settings(turn_acceleration=125)
     chassis.turn(45)
     chassis.straight(350)
     chassis.turn(-45)
     chassis.straight(219.0000000009)
     chassis.turn(-87)
     #pushing coral
     chassis.settings(300,200)
     chassis.turn(2)
     chassis.straight(90.998)
    #  chassis.straight(-41.0009)
     #taking dude   
     arm_right.run_angle(400, -550.09)
     chassis.straight(-76)
     chassis.straight(-41.0009)

     chassis.turn(34)
     #shark
     chassis.settings(900.2,900)
     chassis.straight(280)
     chassis.settings(367,299)
     chassis.straight(-325.003001)
     #moving
     chassis.turn(30.3)
     chassis.straight(-40)
     chassis.turn(12)
     chassis.settings(600,700)
     #puting dude
     arm_right.run_angle(-400,-30)
     chassis.straight(80)
     wheel_right.run_angle(300,-24)
     chassis.straight(-15)
     arm_right.run_angle(-400,-550.09)
    #  wheel_right.run_angle(300,30)
     #geting home 
     chassis.straight(-100)
     chassis.settings(600,500)
     chassis.curve(-500,-90)
    




def run_3():
    #pushing ship
    arm_right.run_angle(100,100, wait=False)
    arm_left.run_angle(400,-100,wait=False)
    chassis.settings(246,327)
    chassis.straight(-650.42)
    chassis.straight(50.42)
    chassis.straight(-300)
    #pulling crabs
    chassis.settings(100,50)
    chassis.straight(220)
    #moving
    chassis.turn(-160)
    chassis.settings(500, 500)
    chassis.straight(100)
    chassis.curve(-200, 35)
    chassis.straight(100)
    chassis.curve(100, -70)
    chassis.straight(100)
    #puting shark
    arm_left.run_angle(400,-200,wait=False)
    arm_right.run_angle(-200,50)
    chassis.straight(-68)
    #going home
    chassis.turn(80)
    chassis.straight(400)
    chassis.curve(500,90)


    #chassis.straight(-170)
    #chassis.turn(-60)
    #taking shrimp
    #arm_left.run_angle(500,400,wait=False)
    #wait(200)
    #chassis.straight(170)
    #chassis.straight(-20)
    #arm_left.run_angle(-200,400)
    #chassis.turn(-60)



def run_4():
    arm_left.run_angle(300,400)

def run_5():
    arm_left.run_angle(300,400)
def run_9():
    chassis.straight(2000)
  


selected = hub_menu("1", "2", "3", "4", "5", "9")


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
