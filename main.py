import text_to_speech

speech = open(file="Introduction")

text_to_speech.speak(speech.read())
