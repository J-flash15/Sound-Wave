#Dec 5,2020
#Final Project 
#Description: This program will record sound and then plot it on a graph.
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave


#this is the variables that will be used in the program
FRAMEBUFFER = 6400
FORMAT = pyaudio.paInt32
CHANNELS = 1 
RATE = 16000


#this is the function that will record the sound
sound = pyaudio.PyAudio()

#this is the function that will record the sound
streams = sound.open( 
	format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
	frames_per_buffer=FRAMEBUFFER

)


print("beginning recording")


minutes = 2
frames = []
minutes_tracking = 0
minutes_count = 0 

#this is the loop that will record the sound
for i in range(0, int(RATE/FRAMEBUFFER*minutes)):

	input = streams.read(FRAMEBUFFER)

	frames.append(input)
	minutes_tracking += 1 

	if minutes_tracking == RATE/FRAMEBUFFER:

		minutes_count += 1 

		minutes_tracking = 0 

		print(f'Time left:{minutes_count} minutes')


#this is the function that will stop the recording
streams.stop_stream()
streams.close()
sound.terminate()

#this is the function that will save the recording
sham = wave.open('sound.wav', 'wb')
sham.setnchannels(CHANNELS)
sham.setsampwidth(sound.get_sample_size(FORMAT))
sham.setframerate(RATE)
sham.writeframes(b''.join(frames))
sham.close()

#this is the function that will plot the sound wave
file = wave.open('sound.wav', 'rb')

#this is the variables that will be used in the program
test = file.getframerate()
frames = file.getnframes()
sound_wave = file.readframes(-1)

#this is the function that will close the file
file.close()


time = frames / test 


#this is the function that will plot the sound wave
sound_array = np.frombuffer(sound_wave, dtype=np.int64)

#this is the function that will plot the sound wave
times = np.linspace(0, time, num=frames)


#this is the function that will plot the sound wave
plt.figure(figsize=(100, 400))
plt.plot(times, sound_array)
plt.ylabel("sound wave")
plt.xlabel('Time (m)')
plt.xlin(0, time)
plt.title('what i am recoding!!')
plt.show()


