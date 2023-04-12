import matplotlib.pyplot as plt
import wave
import numpy as np
from scipy.signal import find_peaks


wavFile =["PDC RHD Recording\Final_R.wav","PDC RHD Recording\\nr_R.wav"]
print("wavfile=",wavFile)
plt.rcParams["figure.autolayout"] = True
yff=[]
xff=[]
xt=[]
yt=[]
#fig, (ax1,ax2) = plt.plot(figsize=(15, 7))
for i in range (len(wavFile)):
    wavposition= wavFile[i]
    wav_obj = wave.open(wavposition, 'rb')
    sample_freq = wav_obj.getframerate()
    n_samples = wav_obj.getnframes()
    t_audio = n_samples/sample_freq
    n_channels = wav_obj.getnchannels()
    signal_wave = wav_obj.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    l_channel = signal_array[0::1]

    times = np.linspace(0, n_samples/sample_freq, len(l_channel))

    xt.append(times)
    yt.append(l_channel)

    plt.plot(xt[i],yt[i],alpha=0.5)
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
plt.show()
