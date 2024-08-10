from utils.CONSTANTS import *
import serial
import numpy as np


# Description: Read audio buffer from serial port
# Returns: np int16 arraythat is FFT_SIZE long
def SERIAL_read_audio_buffer() -> bytes:
    ser = serial.Serial(SERIAL_PORT, BAUDRATE)
    audio_bytes = ser.read(NUM_BYTES_AUDIO)

    # Convert bytes to int16
    audio_buffer = np.frombuffer(audio_bytes, dtype=np.int16)
    return audio_buffer


