from utils.CONSTANTS import *
from utils.SERIAL import *
from FFT_Analysis.PLOT import *

import numpy as np
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    ser = serial.Serial(SERIAL_PORT, BAUDRATE)
    fig, ax = plt.subplots()
    x: np.ndarray = np.full(FFT_SIZE, SEC_BETWEEN_DATA)
    y: np.ndarray = np.zeros(FFT_SIZE)
    line, = ax.plot(x, y)
    ax.set_ylim(-32768, 32767)  # int16 range

    # ani = animation.FuncAnimation(fig, update_plot, fargs=(line, ser), interval=SEC_BETWEEN_DATA * 1000, blit=True)
    ani = animation.FuncAnimation(fig, update_plot, fargs=(line, ser), blit=True)
    plt.show()

    # while True:
    #     audio_buffer: np.ndarray = SERIAL_read_audio_buffer()
    #     print(audio_buffer.size)
    #     PLOT_audio_buffer(audio_buffer)


if __name__ == '__main__':
    main()
    