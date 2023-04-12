from pydub import AudioSegment

front = AudioSegment.from_file("PDC RHD Recording\Final_F.wav")
rear = AudioSegment.from_file("PDC RHD Recording\Final_R.wav")


for i in range (15):

    diff = float(i)

    front_red = front.apply_gain_stereo(diff, diff)
    rear_red = rear.apply_gain_stereo(diff, diff)

    front_file = "PDC Combined RHD\F_" + str(diff) + "db.wav"
    rear_file = "PDC Combined RHD\R_" + str(diff) + "db.wav"

    front_red.export(front_file, format="wav")
    rear_red.export(rear_file, format="wav")