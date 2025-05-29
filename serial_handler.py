import serial
from serial.serialutil import SerialException
import time
import config

class ArduinoManager:
    def __init__(self):
        self.ser = None
        self.connected = False
        self.init_serial()
    
    def init_serial(self):
        """Initialize the serial connection and pause execution
        for 2 second to allow the serial connection to establish properly"""
        try:
            self.ser = serial.Serial(config.COM_PORT, config.BAUD_RATE)
            time.sleep(2)
            self.connected = True
        except:
            self.connected = False
    
    def write_data(self, data: bytes):
        self.ser.write(data) 
