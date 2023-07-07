class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.sensor_range = 0
        self.direction = 0


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(f"Motor Speed: {robot_1.motor_speed}")
print(f"Direction: {robot_1.direction}")
print(f"Sensor Range: {robot_1.sensor_range}")


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
