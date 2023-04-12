import wave
import numpy as np
from scipy.io import wavfile
import noisereduce as nr
from pydub import AudioSegment

class Wav:

    def __init__(self,wavposition,nrposition):
        self.wavpos = wavposition
        self.nrpos = nrposition
        
    def open(self,position):

        wav_obj = wave.open(position, 'rb')
        n_samples = wav_obj.getnframes()
        signal_wave = wav_obj.readframes(n_samples)
        signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        signal = signal_array

        return signal

    def get_rate(self):

        rate, data = wavfile.read(self.wavpos)

        return rate

    def noise_reduce(self):

        signal = self.open(self.wavpos)
        rate = 2* self.get_rate()
        reduced_noise = nr.reduce_noise(y=signal, sr=rate, freq_mask_smooth_hz=200)
        wavfile.write(self.nrpos,int(rate), reduced_noise)
    
    def trim(self):

        rate = self.get_rate()
        data = self.open(self.nrpos)
        data=data.tolist()
        
        fbar = 0.3*max(data)
        rbar = 0.1*max(data)

        i=0
        while True:
            i+=10
            if data[i] > fbar:
                i=i-10
                while True:
                    i+=1
                    if data[i] > fbar:
                        start=i/rate*1000
                        break
                break

        i=0
        while True:
            i+=1
            j=len(data)-i
            if data[j] > rbar:
                i=i-10
                while True:
                    i+=1
                    j=len(data)-i
                    if data[j] > rbar:
                        end=j/rate*1000
                        break
                break

        part_1 = AudioSegment.from_file(self.nrpos)
        trimmed = part_1[start:end]
        trimmed.export(".\\temp\\trimmed_nr.wav", format="wav")
        data = np.copy(self.open(".\\temp\\trimmed_nr.wav"))
        outname=".\\temp\\pre.wav"
        wavfile.write(outname, rate, data)

    def len_match(self,signal):
        
        for i in range (220500-len(signal)):
            signal.append(0)
        return signal


if __name__ == "__main__":
    wav = Wav("PDC RHD Recording\Final_R.wav","PDC RHD Recording\\nr_R.wav")
    wav.noise_reduce()