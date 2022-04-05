import pyttsx3 as Ptx

# Speaker
Speaker = Ptx.init()

# Text reader
def reader(Text):
    Speaker.say(Text)
    Speaker.runAndWait()
