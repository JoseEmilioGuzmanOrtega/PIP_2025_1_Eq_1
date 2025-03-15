# pyserial .....
import serial as control

arduino = control.Serial("COM5", baudrate=9600, timeout=1)

while True:
    v = input("Valor de Control para el led: ")
    arduino.write(v.encode())