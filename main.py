import cozmo

def cozmoProgram(robot: cozmo.robot.Robot):
    print(f"Current battery level: {robot.battery_voltage} %")

    robot.say_text("Hello, world!").wait_for_completed()
    robot.say_text(f"Current battery level: {round(robot.battery_voltage, 4)} %")

    robot.wait_for_all_actions_completed()


cozmo.run_program(cozmoProgram)
