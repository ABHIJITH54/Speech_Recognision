import speech_recognition as sr

def recognize_speech_from_microphone():
    recognizer=sr.Recognizer()
    mic=sr.Microphone()
    while True:
        try:
            with mic as source:
                print("please speak something")
                audio=recognizer.listen(source)
                print("Recognizing")
                text=recognizer.recognize_google(audio)   #api google
                print(f"you said: {text}")
                # return text
                if text.lower()=="stop":
                    break
        except sr.UnknownValueError:
            print("sorry i did not understand you")
        except sr.RequestError as e:
            print(f"An error occured : {e}")

recognize_speech_from_microphone()