import speech_recognition as sr

r = sr.Recognizer()

audio = 'record.wav'


with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)
    saveFile=open('mcq.txt','w')
    saveFile.write(text)
    saveFile.close()
    
except Exception as e:
    print (e)


##with sr.Microphone() as source:
##    audio=r.listen(source)
