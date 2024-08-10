import serial

# Open /dev/ttyUSB0

ser = serial.Serial('/dev/ttyUSB0', 112500)

# Continually read from the serial port

while True:
    print(ser.readline().decode('utf-8'), end='')   
