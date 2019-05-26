import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
np.seterr(divide = 'ignore') 

def scaled_fft_db(x):
    """ ASSIGNMENT 1:
        a) Compute a 512-point Hann window and use it to weigh the input data.
        b) Compute the DFT of the weighed input, take the magnitude in dBs and
        normalize so that the maximum value is 96dB.
        c) Return the first 257 values of the normalized spectrum

        Arguments:
        x: 512-point input buffer.

        Returns:
        first 257 points of the normalized spectrum, in dBs
    """

    # Your code goes here
    # a) Compute a 512-point Hann window and use it to weigh the input data.
    N = len(x)
    #plt.title("x_array")
    #plt.plot(x)
    #plt.show()

    window = np.hanning(N)
    #plt.title("Hann window")
    #plt.plot(window)
    #plt.show()

    # # Compute the fft of x, normalized by the size of the input
    dft = np.fft.rfft(x * window) / N

    # Keep only the first N/2+1 samples of the FFT
    dft = dft[0: np.int(N/2+1)]

    # Take the magnitude of dft
    mag = np.abs(dft)

    # Convert the magnitudes to dB
    spectrum = 20 * np.log10(mag)
    spectrum[np.isneginf(spectrum)]=-100.

    # Rescale to amx of 96 dB
    max_db = np.amax(spectrum)
    spectrum = 96-max_db + spectrum

    plt.title("spectrum DFT(x*w)")
    plt.plot(spectrum)
    plt.show()
    return spectrum[:257]


if __name__ == "__main__":

    def check_assignment1():

        pass_test = True

        for i in range(1,5):
            print ('  Test %d:' % (i))
            fin = 'data/testInput' + str(i) + '.wav'
            fout = 'data/testOutput' + str(i) + '.wav'

            r,x = wavfile.read(fin)

            # compute output of assignment function
            X = scaled_fft_db(x)

            print ('    Signal size is 257:',)
            if X.shape[0] == 257:
                print ('okay')
            else:
                print ('fail')
                pass_test = pass_test and False

            print ('    Maximum is 96 dB:',)
            if np.abs(X.max() - 96) < 1e-5:
                print ('okay')
            else:
                print ('fail')
                pass_test = pass_test and False

            # compare to test output file content
            X_check = np.loadtxt(fout)

            print ('    Test signals output match:',)
            if np.allclose(X, X_check,atol=1e-1):
                print ('okay')
            else:
                print ('fail')
                pass_test = pass_test and False

        print ('  Test hanning window:'),
        x = np.ones(512)
        x[1:-1] = 1./np.hanning(512)[1:-1]
        X = scaled_fft_db(x)
        win_test = np.zeros(257)
        win_test[0] = 96

        if X[0] == 96 and np.all(X[1:] < 50):
            print ('okay')
        else:
            print ('fail')
            pass_test = pass_test and False

        if pass_test:
            print ('Congratulations, your algorithm passed all the tests.')
        else:
            print ('Sorry, your algorithm is not ready for submission yet.')
    check_assignment1()