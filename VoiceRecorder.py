import lineup_engine
import pyaudio
import wave

chunk = 3024
pyaudioIntFormat = pyaudio.paInt16
channels = 1
rate = 44100
py = pyaudio.PyAudio()
global page


class VoiceRecorder:

    def __init__(self, window):
        global page
        self.collections = []
        self.CHUNK = chunk
        self.FORMAT = pyaudioIntFormat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1

        page = window
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                  frames_per_buffer=self.CHUNK)

    def start_record(self):
        global page
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                             frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            # Comment out only for debugging
            # print("* recording")
            page.update()

        stream.close()

        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.st = 0
