import serial, time


def Arranque():
    arduino = serial.Serial("COM5", 9600,timeout=1)
    arduino.reset_input_buffer()
    arduino.reset_output_buffer()
    time.sleep(1)
    x= arduino.read_all()
    print (x)
    print("enviando")
    arduino.write(b'3')
    arduino.reset_input_buffer()
    arduino.reset_output_buffer()
    arduino.close()

