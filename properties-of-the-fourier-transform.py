# https://dspillustrations.com/pages/posts/misc/properties-of-the-fourier-transform.html


def ft(samples, Fs, t0):
    """Approximate the Fourier Transform of a time-limited signal 
    by means of the discrete Fourier Transform.
    
    samples: signal values sampled at the positions t0 + n/Fs
    Fs: Sampling frequency of the signal
    t0: starting time of the sampling of the signal
    """
    f = np.linspace(-Fs/2, Fs/2, len(samples), endpoint=False)
    return np.fft.fftshift(np.fft.fft(samples)/Fs * np.exp(-2j*np.pi*f*t0))



