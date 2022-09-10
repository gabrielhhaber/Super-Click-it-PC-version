import random
from pythonBgt import *
onePlayer=loadSound("voice/one player.ogg")
twoPlayer=loadSound("voice/two player.ogg")
onePoint=loadSound("sound/1point.ogg")
tenPoints=loadSound("sound/10points.ogg")
squish=loadSound("sound/squish.ogg")
squishCmd=loadSound("command/squish.ogg")
blast=loadSound("sound/blast.ogg")
blastCmd=loadSound("command/blast+kick.ogg")
crack=loadSound("sound/crack.ogg")
crackCmd=loadSound("command/crack+kick.ogg")
zip=loadSound("sound/zip.ogg")
zipCmd=loadSound("command/zip+kick.ogg")
twist=loadSound("sound/twist.ogg")
twistCmd=loadSound("command/twist+kick.ogg")
switchCmd=loadSound("command/switch.ogg")
winSound=loadSound("sound/win.ogg")
err1=loadSound("sound/Fail boing.ogg")
err2=loadSound("sound/Fail flip crash.ogg")
err3=loadSound("sound/Fail owowowo.ogg")
err4=loadSound("sound/Fail Ricaushay boom.ogg")
err5=loadSound("sound/Fail wah wah wah warrrrr.ogg")
errs=[err1, err2, err3, err4, err5]
cmt1=loadSound("comment/No way.ogg")
cmt2=loadSound("comment/Oh no.ogg")
cmt3=loadSound("comment/Sorry.ogg")
cmts=[cmt1, cmt2, cmt3]
musicSpeed1=loadSound("sound/Music beat speed1.ogg")
musicSpeed2=loadSound("sound/Music beat speed2.ogg")
musicSpeed3=loadSound("sound/Music beat speed3.ogg")
musicSpeed4=loadSound("sound/Music beat speed4.ogg")
musicSpeed5=loadSound("sound/Music beat speed5.ogg")
mode=1
def playModeSound(modeNumber):
	if modeNumber==1:
		onePlayer.playWait()
		squishCmd.playWait()
	elif modeNumber==2:
		onePlayer.playWait()
		squish.playWait()
	elif modeNumber==3:
		twoPlayer.playWait()
		squishCmd.playWait()
	elif modeNumber==4:
		twoPlayer.playWait()
		squish.playWait()
def playGame():
	commands={
"squish": squishCmd,
"blast": blastCmd,
"crack": crackCmd,
"zip": zipCmd,
"twist": twistCmd,
}
	if mode==3 or mode==4:
		commands["switch"]=switchCmd
	commandsList=list(commands.keys())
	keys={
"squish": K_TAB,
"crack": K_RETURN,
"blast": K_SPACE,
"zip": K_BACKSPACE,
"twist": K_RSHIFT,
}
	sounds={
"squish": squish,
"blast": blast,
"crack": crack,
"zip": zip,
"twist": twist,
"switch": switchCmd,
}
	music=musicSpeed1
	points=0
	while points<100:
		wait(5)
		correct=False
		command=random.choice(commandsList)
		if mode==1 or mode==3:
			commands[command].play()
		elif mode==2 or mode==4:
			sounds[command].play()
		music.stop()
		if command=="switch":
			correct=True
			music.playWait()
			music.playWait()
		else:
			music.play()
		while music.playing and music.timeLeft>100:
			wait(5)
			for key in keys:
				if not correct and keyPressed(keys[key]):
					if keys[key]==keys[command]:
						if command=="blast":
							wait(300)
							if not keyDown(keys[command]):
								break
						correct=True
						points+=1
						if mode==1 or mode==3:
							sounds[command].play()
					else:
						correct=False
						music.stop()
		if not correct:
			error(points)
			break
		if points==20:
			music=musicSpeed2
		elif points==40:
			music=musicSpeed3
		elif points==60:
			music=musicSpeed4
		elif points==80:
			music=musicSpeed5
	else:
		win()

def error(points):
	err=random.choice(errs)
	err.playWait()
	wait(100)
	cmt=random.choice(cmts)
	cmt.playWait()
	wait(100)
	while points>=10:
		points-=10
		tenPoints.playWait()
		wait(100)
	while points>=1:
		points-=1
		onePoint.playWait()
		wait(100)
def win():
	winSound.playWait()

showWindow("Super Click it! PC version")
playModeSound(mode)
while not keyPressed(K_ESCAPE):
	if keyPressed(K_TAB):
		mode=mode+1 if mode<4 else 1
		playModeSound(mode)
	if keyPressed(K_RETURN):
		playGame()
	wait(5)