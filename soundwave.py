from signal import signal
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave, sys

FRAMEBUFFER = 6400
FORMAT = pyaudio.paInt32
channels = 1 
rate = 16000



sound = pyaudio.PyAudio()
stream = sound.open(format = FORMAT,  channels=channels, 
rate=rate, input=True, frames_per_buffer=FRAMEBUFFER)


print("begining recording")

times = 5
frame = []
time_tracking = 0
time_count = 0 

audiofile =  wave.open('sound.wav', 'rb')


frame = audiofile.getnframes()
signal = audiofile.readframes(-1)
signal = np.frombuffer(signal, dtype= "int16")
f_rate = audiofile.getframerate()

audiofile = wave.open('sound.wav', 'wb')
audiofile.setnchannels(channels)
audiofile.setsampwidth(sound.get_sample_size(FORMAT))
audiofile.writeframes(b''.join(frame))

for i in range(0, int(rate/FRAMEBUFFER*times)):

	time = np.linspace(0,len(signal)/ f_rate, num = len(signal))
     
	data = stream.read(FRAMEBUFFER)
	frame.append(data)
	time_count += 1

	if time_tracking == rate/FRAMEBUFFER:
		time_count += 1 
		time_tracking = 0 

		print(f'Time Left: {times - time_count} times')


	plt.figure(figsize=(100, 400))

	plt.title("sound Wave")
	plt.xlabel("Time")
	plt.plot(time, signal)
	plt.show()


if __name__ == "_main_":

	path = sys.argv[1]
