#Simple way to read and print some samples
from rtlsdr import RtlSdr
from math import e
import numpy as np 
import sys

#def read_print_samples(sample_rate, center_freq, freq_correction):
def read_print_samples(center_freq):
    """
    input:
    center_freq.- Get/Set the center frequency of the device (in Hz)

    output:
    samples.- numpy array
    """
    sdr = RtlSdr()
    
    # configure device
    """
    sdr.sample_rate = 2.048e6  # Hz
    sdr.center_freq = 70e6     # Hz
    sdr.freq_correction = 60   # PPM
    """
    sdr.center_freq = center_freq     # Hz 

    sdr.sample_rate =  230000 #66KHz
    """
    #Teorema de Nyquist  # Hz
    sample_rate óptimo: 2B
    Frecuencia de muestreo debe ser dos veces el ancho de banda
    """
    sdr.freq_correction = 1   # PPM
    sdr.gain = 'auto'
    
    samples = sdr.read_samples(512) #number  of  samples  or  bytes  to  read 

    np.savetxt('samples_real.txt', samples.real, fmt='%10.15f' )
    np.savetxt('samples_imag.txt', samples.imag, fmt='%10.15f' )
    ##Por ahora lo voy a guardar como txt, pero seguiré en la busqueda de un formato mejor para la transferencia de archivos. 
    ##npy parecía buena opción
    #np.save('samples.npy',samples)


if __name__=="__main__":
    #print(read_print_samples( int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]) ) )
    read_print_samples( int(sys.argv[1]) ) #Frecuencia central (estación de radio)