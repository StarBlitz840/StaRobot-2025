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
# arm_right = Motor(Port.F)
# arm_left = Motor(Port.B)
# wheel_right = Motor(Port.D)
# wheel_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
# back_sensor = ColorSensor(Port.E)
# front_sensor = ColorSensor(Port.C)
# chassis = DriveBase(wheel_left, wheel_right, 62.4, 100)
arm_right = Motor(Port.C)
arm_left = Motor(Port.B)
wheel_right = Motor(Port.E)
wheel_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
back_sensor = ColorSensor(Port.F)
front_sensor = ColorSensor(Port.A)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 100)
chassis.use_gyro(True)
hub.imu.reset_heading(0)
chassis.settings(straight_speed=250,turn_rate=100)

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

arm_right.run_time(120, 3000)