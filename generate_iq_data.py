"""
Saves data in a binary file of real and imaginary signals
Copyright (C) 2021 Juan Luis Ruiz Vanegas (juanluisruiz971@comunidad.unam.mx)
"""

from rtlsdr import RtlSdr
import numpy as np
import sys
import os.path
from datetime import date
from pathlib import Path


def read_print_samples(center_freq: float):
    """
    input:
    center_freq.- Get/Set the center frequency of the device (in Hz)
    output:
    samples.iq .- binary file
    """
    sdr = RtlSdr()

    #--- Default values ---#
    sdr.center_freq = center_freq   # Hz
    # sdr.sample_rate =  230000#center_freq * 2 #(230KHz min samples by sec) Muestras por segundo
    sdr.sample_rate = 1.024e6  # (Msps)
    sdr.freq_correction = 'auto'  # PPM
    sdr.gain = 'auto'

    number_samples = (256*1024)   # number  of  samples  or  bytes  to  read
    samples = sdr.read_samples(number_samples)

    #--- Now save to an IQ file ----#
    samples = samples.astype(np.complex64)  # Convert to 64

    ##---- Check if directory exists... if not, create it   ---##
    date_ = date.today()
    PATH = 'samples/'+str(date_.year)+'/'+str(date_.month)+'/'+str(date_.day)
    Path(PATH).mkdir(parents=True, exist_ok=True)

    filename = 'number_samples:' + \
        str(number_samples)+"-center_freq:"+str(center_freq)+'_Mhz.iq'
    SAVE = os.path.join(PATH, filename)
    samples.tofile(SAVE)  # Save to file
    print("file {} created at \n\t\t{}".format(filename, PATH))

    """
    In Python, the default complex type is np.complex128, which uses two 64-bit floats per sample. 
    But in DSP/SDR, we tend to use 32-bit floats instead because the ADCs on our SDRs don’t have that
     much precision to warrant 64-bit floats. In Python we will use np.complex64, which uses two 
     32-bit floats. When you are simply processing a signal in Python it doesn’t really matter, 
     but when you go to save the 1d array to a file, you want to make sure it’s an array of 
     np.complex64 first.
     https://pysdr.org/content/iq_files.html
    """


if __name__ == "__main__":
    # Center frequency (radio station [Hz])
    read_print_samples(sys.argv[1])


"""
To Run the code:
    python3 generate_iq_data.py <Radio station in Hertz>
    python3 generate_iq_data.py 102500000
        96.7MHz
"""
