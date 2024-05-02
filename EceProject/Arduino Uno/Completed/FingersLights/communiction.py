import serial

# Establish serial communication
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port


# Function to turn the light on
def light_on():
    command = b'1'  # Send '1' to Arduino to turn light on
    arduino.write(command)


# Function to turn the light off
def light_off():
    command = b'0'  # Send '0' to Arduino to turn light off
    arduino.write(command)


def sendCommend(command):
    if command == 1:
        command = b'1'  # Send '0' to Arduino to turn light off
    elif command == 2:
        command = b'2'
    elif command == 3:
        command = b'3'
    elif command == 4:
        command = b'4'
    elif command == 5:
        command = b'5'
    else:
        command = b'0'
    arduino.write(command)

# Example usage:
#
# while True:
#     light_on()  # Turn the light on
#     # ... (Do other things)
#     time.sleep(1)
#     light_off()  # Turn the light off
#     time.sleep(0.3)
