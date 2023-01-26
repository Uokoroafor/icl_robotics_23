import BrickPi3
BP = BrickPi3()

PORT_SENSOR_IR = BP.PORT_1
PORT_MOTOR_RIGHT = BP.PORT_A
PORT_MOTOR_LEFT = BP.PORT_D

#Move Forward
def fwd():
    BrickPi3.MotorSpeed[PORT_MOTOR_RIGHT] = speed
    BrickPi3.MotorSpeed[PORT_MOTOR_LEFT] = speed
#Move Left
def left():
    BrickPi3.MotorSpeed[PORT_MOTOR_RIGHT] = speed
    BrickPi3.MotorSpeed[PORT_MOTOR_LEFT] = -speed
#Move Right
def right():
    BrickPi3.MotorSpeed[PORT_MOTOR_RIGHT] = -speed
    BrickPi3.MotorSpeed[PORT_MOTOR_LEFT] = speed
#Move backward
def back():
    BrickPi3.MotorSpeed[PORT_MOTOR_RIGHT] = -speed
    BrickPi3.MotorSpeed[PORT_MOTOR_LEFT] = -speed
#Stop
def stop():
    BrickPi3.MotorSpeed[PORT_MOTOR_RIGHT] = 0
    BrickPi3.MotorSpeed[PORT_MOTOR_LEFT] = 0

"""
BrickPi3Setup() # setup the serial port for communication

PORT_MOTOR_RIGHT = BP.PORT_A
PORT_MOTOR_LEFT = BP.PORT_D
BrickPi3.MotorEnable[PORT_MOTOR_RIGHT] = 1 #Enable the Motor A
BrickPi3.MotorEnable[PORT_MOTOR_LEFT] = 1 #Enable the Motor B
BrickPi3SetupSensors() #Send the properties of sensors to BrickPi
BrickPi3.Timeout=10000 #Set timeout value for the time till which to run the motors after the last command is pressed
BrickPi3SetTimeout() #Set the timeout


BrickPi3UpdateValues() #Update the motor values
"""