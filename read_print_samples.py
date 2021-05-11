#Simple way to read and print some samples
from rtlsdr import RtlSdr
from math import e
import sys

def read_print_samples(sample_rate, center_freq, freq_correction):
    sdr = RtlSdr()
    #input from console
    
    #print(type(sample_rate), type(center_freq), type(freq_correction))    
    
    # configure device
    """
    sdr.sample_rate = 2.048e6  # Hz
    sdr.center_freq = 70e6     # Hz
    sdr.freq_correction = 60   # PPM
    """
    sdr.sample_rate = sample_rate  # Hz
    sdr.center_freq = center_freq     # Hz
    sdr.freq_correction = freq_correction   # PPM
    sdr.gain = 'auto'
    
    return(sdr.read_samples(512))


if __name__=="__main__":
    print(read_print_samples( int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]) ) )