from utils.CONSTANTS import *
from utils.SERIAL import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import serial



def PLOT_update(i):
    time_vals: np.ndarray = np.linspace(0, SEC_BETWEEN_DATA, FFT_SIZE)          # x-axis
    audio_buffer: np.ndarray = SERIAL_read_audio_buffer()                       # y-axis
    
    plt.cla()
    plt.axis([0, SEC_BETWEEN_DATA, -32768, 32767])
    plt.plot(time_vals, audio_buffer)
    plt.tight_layout()


def PLOT_init():
    # plt.style.use('fivethirtyeight')
    matplotlib.use('Qt5Agg')                # Use an interactive backend


def PLOT_get_animation():
    PLOT_init()                         # Initialize plot

    ani = animation.FuncAnimation(plt.gcf(), PLOT_update, interval=PLT_INTERVAL_AUDIO, cache_frame_data=False)
    return ani

def main():
    ani = PLOT_get_animation()
    plt.show()

if __name__ == '__main__':
    main()
    