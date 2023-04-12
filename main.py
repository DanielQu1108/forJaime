import argparse
import pyaudio
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pydub import AudioSegment

def main(args):
    if args.r:
        print("Record Sound")
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                
                if "Umik" in p.get_device_info_by_host_api_device_index(0, i).get('name'):
                    device_index=i
                    print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 30
        WAVE_OUTPUT_FILENAME = ".\PDC Recordings\\Final_R.wav"
        
        audio = pyaudio.PyAudio()
        
        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK, input_device_index=device_index)
        print ("recording...")
        frames = []
        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print ("finished recording")
        
        
        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

    if args.p:
        print("Plot Sound")
        wavFile =["PDC Recordings\\Final_R.wav"]
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

    if args.l:
        print("Loudness Check")
        sound = AudioSegment.from_file("PDC Recordings\\6HZ_F.wav")
        sound_RE = AudioSegment.from_file("PDC Recordings\\6HZ_F_RE.wav")

        loudness = sound.dBFS
        loudness_RE = sound_RE.dBFS

        diff = loudness-loudness_RE
        print(diff)

        # make left channel 6dB quieter and right channe 2dB louder
        sound_RE_adjusted = sound.apply_gain_stereo(diff, diff)

        sound_RE_adjusted.export("PDC Adjusted\\6HZ_F.wav", format="wav")

    if args.rl:
        print("Loudness Check")

        sound = AudioSegment.from_file("PDC Recordings\\Const_R.wav")

        diff=-9.75
        
        sound_RE_adjusted = sound.apply_gain_stereo(diff, diff)

        sound_RE_adjusted.export("PDC Adjusted\\Const_R.wav", format="wav")

    if args.fl:
        print("Loudness Check")

        sound = AudioSegment.from_file("PDC Recordings\\Roger_F.wav")

        diff=-4.928
        
        sound_RE_adjusted = sound.apply_gain_stereo(diff, diff)

        sound_RE_adjusted.export("PDC Adjusted\\Roger_F.wav", format="wav")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action="store_true", help="record sound")
    parser.add_argument("-p", action="store_true", help="plot sound")
    parser.add_argument("-l", action="store_true", help="loudness match")
    parser.add_argument("-rl", action="store_true", help="rear loudness match, db-9.57")
    parser.add_argument("-fl", action="store_true", help="front loudness match, db-9.57")
    args = parser.parse_args()
    main(args)