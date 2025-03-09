#!"/home/dia/Documents/,code/CozmoSDK Playground/.venv/bin/python"

import cozmo
from cozmo.util import *

# COMMAND FOR STARTING IOS WEIRD USB THING ON LINUX:
# -=-=-=-=-= sudo usbmuxd -f -v =-=-=-=-=-
# check with `ideviceinfo`


def cozmoProgram(robot: cozmo.robot.Robot):
    print(f"Current battery level: {robot.battery_voltage} %")

    # robot.say_text("Hello world!", duration_scalar=0.5).wait_for_completed()
    robot.say_text(f"Current battery level: {round(robot.battery_voltage, 2)} %", duration_scalar=0.5).wait_for_completed()

    robot.drive_straight(distance_mm(1000), speed_mmps(200)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    robot.wait_for_all_actions_completed()


cozmo.run_program(cozmoProgram)
