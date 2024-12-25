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
    arm_left.run_angle(250, 95, wait=False)
    arm_right.run_angle(250, -95)
    chassis.settings(350)
    chassis.straight(510)
    arm_right.run_angle(250, 120, wait=False)
    arm_left.run_angle(250, -120)
    chassis.settings(250,100)
    chassis.straight(-225)
    chassis.turn(-106)
    chassis.straight(-250)
    chassis.settings(500,500,300)
    chassis.straight(240)
    chassis.turn(110)
    chassis.straight(-350)









def run_2():
     #צוללן אלמוגים
     chassis.settings(251.7,567.8)
     chassis.settings(403.0032)
     chassis.straight(200.0908)
     chassis.turn(45)
     chassis.straight(350)
     chassis.turn(-45)
     chassis.straight(219.0000000009)
     chassis.turn(-87)
     chassis.settings(700,1203)
     chassis.straight(78.998)
     chassis.straight(-28.0009)     
     arm_right.run_angle(400, -500.09)
     chassis.straight(-76)
     chassis.turn(40)
     chassis.settings(653.2,1078)
     chassis.straight(238)
     chassis.settings(367,299)
     chassis.straight(-331)
     chassis.turn(45.3)
     arm_right.run_angle(100, 50.09)
     chassis.straight(79.7)
     arm_right.run_angle(-400,-200.09)






def run_3():
    pass

def run_4():
    pass

def run_5():
    pass
def run_9():
    pass


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
