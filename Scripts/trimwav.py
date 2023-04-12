from pydub import AudioSegment

# Import part 1 and part 2 audio files
file="PDC RHD Recording\Final_R.wav"

part_1 = AudioSegment.from_file(file)
# Remove the first four seconds of part 1
trimmed = part_1[2440:32440]

# rsilence = AudioSegment.silent(duration=20000)
# trimmed = trimmed + rsilence
# trimmed = trimmed[:10000]

trimmed.export(file, format="wav")

