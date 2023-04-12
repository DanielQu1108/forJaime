from pydub import AudioSegment

file=".\PDC Recordings\Front_1khz.wav"

part_1 = AudioSegment.from_file("PDC Recordings\Roger_F.wav")

part_2 = AudioSegment.from_file("PDC Recordings\\1HZ_F.wav")

part_3 = AudioSegment.from_file("PDC Recordings\\2HZ_F.wav")

part_4 = AudioSegment.from_file("PDC Recordings\\4HZ_F.wav")

part_5 = AudioSegment.from_file("PDC Recordings\\6HZ_F.wav")

part_6 = AudioSegment.from_file("PDC Recordings\Const_F.wav")

mix = part_1 + part_2 + part_3 + part_4 + part_5 + part_6

mix.export("PDC Recordings\Final_F.wav", format="wav")