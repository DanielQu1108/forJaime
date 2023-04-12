from pydub import AudioSegment


# diff = loudness-loudness_RE
# print(diff)

# # make left channel 6dB quieter and right channe 2dB louder
# sound_RE_adjusted = sound.apply_gain_stereo(diff, diff)

# sound_RE_adjusted.export("PDC Recordings\Front_1khz_RE_adj.wav", format="wav")

sound = AudioSegment.from_file("PDC Recordings\Final_F.wav")

sound_RE_adjusted = sound.apply_gain_stereo(9.5, 9.5)

sound_RE_adjusted.export("PDC RHD Recording\Final_F.wav", format="wav")

sound = AudioSegment.from_file("C:\DanielQu\Audio_Rig_Integration\\temp\\pre.wav")
sound_RE = AudioSegment.from_file("PDC RHD Recording\Final_R.wav")

loudness = sound.dBFS
loudness_RE = sound_RE.dBFS

print(loudness,loudness_RE)

if str(loudness) == "-inf":
    print("GG")