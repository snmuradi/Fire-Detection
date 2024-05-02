import serial

# Establish serial communication
arduino = serial.Serial('COM4', 9600)  # Replace 'COM3' with your port


def sendCommend(command):
    if command == 21:
        command = b'Q'  # Send '0' to Arduino to turn light off
    elif command == 23:
        command = b'E'
    elif command == 43:
        command = b'X'
    elif command == 41:
        command = b'Z'
    elif command == 1:
        command = b'L'
    elif command == 2:
        command = b'W'
    elif command == 3:
        command = b'D'
    elif command == 4:
        command = b'S'
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
