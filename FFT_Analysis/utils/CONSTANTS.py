# Serial Length Constants
INT16_BYTES             : int               = 2
AUDIO_BUFFER_SIZE       : int               = 8192
FFT_SIZE                : int               = AUDIO_BUFFER_SIZE // 2
START_OF_FIRST_HALF     : int               = 0
START_OF_SECOND_HALF    : int               = FFT_SIZE
NUM_FREQ_BINS           : int               = FFT_SIZE // 2
SAMPLE_RATE             : int               = 93750
NUM_BYTES_AUDIO         : int               = INT16_BYTES * FFT_SIZE
BAUDRATE                : int               = 112500
SERIAL_PORT             : str               = '/dev/ttyUSB0'
SEC_BETWEEN_DATA        : float             = (FFT_SIZE / SAMPLE_RATE)

# PLOTTING
PLT_INTERVAL_AUDIO      : float             = (SAMPLE_RATE / FFT_SIZE)