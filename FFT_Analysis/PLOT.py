from utils.CONSTANTS import *
from utils.SERIAL import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import serial
from threading import Thread
import queue
import time


# GLOBALS
audio_queue: queue.Queue = queue.Queue()

def PLOT_serial_reader():
    while True:
        audio_buffer: np.ndarray = SERIAL_read_audio_buffer()
        if audio_queue.qsize() > QUEUE_MAX_SIZE:
            time.sleep(QUEUE_SLEEP)
        audio_queue.put(audio_buffer)


def PLOT_update(i):
    time_vals: np.ndarray = np.linspace(0, SEC_BETWEEN_DATA, FFT_SIZE)          # x-axis
    audio_buffer: np.ndarray = audio_queue.get()                                 # y-axis
            
    plt.cla()
    plt.axis([0, SEC_BETWEEN_DATA, -32768, 32767])
    plt.plot(time_vals, audio_buffer)
    plt.tight_layout()


def PLOT_init():
    matplotlib.use('Qt5Agg')                # Use an interactive backend


def PLOT_get_animation():
    PLOT_init()                         # Initialize plot

    ani = animation.FuncAnimation(plt.gcf(), PLOT_update, interval=PLT_INTERVAL_AUDIO, cache_frame_data=False)
    return ani

def main():
    # Make serial data reader thread to put audio on queue
    serThread = Thread(target=PLOT_serial_reader)
    serThread.daemon = True
    serThread.start()

    ani = PLOT_get_animation()
    plt.show()

if __name__ == '__main__':
    main()
    