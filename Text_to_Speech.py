import pyttsx3 as tts

running = True

def text_to_speech(cmd):
	global running
	engine = tts.init()
	terminate = ['stop','cancel','exit','quit','good bye','bye','see you']

	if cmd in terminate:
		engine.say('Thanks sir, will see you later.')
		running = False
	else:
		engine.say(cmd)
		engine.setProperty('rate', 100)
		engine.setProperty('volume', 1)
		engine.runAndWait()

while running:
	cmd = input('Enter something here, i will say \n')
	text_to_speech(cmd)

