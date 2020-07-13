import pygame
import time
import random

pygame.init()

gray=(127,127,127)
red=(255,0,0)
green=(85,107,47)
white=(255,255,255)
light_blue=(0,76,153)
blue=(0,51,102)
red = (200,0,0)
green = (0,200,0)
light_red = (255,0,0)
light_green = (0,255,0)
yel=(255,153,51)
fnt = pygame.font.SysFont("comicsans", 20)

width=800
height=600
car_width=56
obs_width = 56
obs_height = 125
global high_score
high_score=0
y2=7
pause=False

icon=pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)   
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Turbo")
img=pygame.image.load('image/Car2.jpg')
side=pygame.image.load('image/download12.jpg')
yell=pygame.image.load('image/yellow strip.png')
whi=pygame.image.load('image/strip.jpg')
back=pygame.image.load('image/background.jpg')
back1=pygame.image.load('image/background2.jpg')
right=pygame.image.load('image/001.png')
left=pygame.image.load('image/003.png')
up=pygame.image.load('image/004.png')
down=pygame.image.load('image/002.png')
p=pygame.image.load('image/p.png')

def get_high_score():
    global high_score

    try:
        high_score_file = open("image/high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        #print()
    except IOError:
        print("IOError")
    except ValueError:
        print("ValueError")
 
    return high_score
 
 
def save_high_score(new_high_score):
    try:
        high_score_file = open("image/high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("IOError")

def countdown_background():
	x=380
	y=465
	screen.blit(side,(0,0))
	screen.blit(side,(700,0))
	screen.blit(whi,(110,0))
	screen.blit(whi,(690,0))
	screen.blit(yell,(405,10))
	screen.blit(yell,(405,110))
	screen.blit(yell,(405,210))
	screen.blit(yell,(405,310))
	screen.blit(yell,(405,410))
	screen.blit(yell,(405,510))
	screen.blit(img,(x,y))
	dodge(0,1)

def countdown():

	countdown=True
	while countdown:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()
			screen.fill(gray)
			countdown_background()
			fnt1 = pygame.font.SysFont("comicsans", 100)
			txt = fnt1.render(" READY ", 1, red)
			screen.blit(txt, (270, 200))
			pygame.display.update()
			time.sleep(1)
			screen.fill(gray)
			countdown_background()
			fnt1 = pygame.font.SysFont("comicsans", 100)
			txt = fnt1.render(" STEADY ", 1, yel)
			screen.blit(txt, (255, 200))
			pygame.display.update()
			pygame.mixer.music.load('audio/Honk.wav')
			pygame.mixer.music.play(1)
			time.sleep(1)
			screen.fill(gray)
			countdown_background()
			fnt1 = pygame.font.SysFont("comicsans", 100)
			txt = fnt1.render(" GO!! ", 1, green)
			screen.blit(txt, (310, 200))
			pygame.display.update()
			#time.sleep(1)

			gameloop()

def button(msg,x,y,w,h,ic,ac,fc,action=None):    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
        	action() 
        
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf = fnt.render(msg, 1, fc)
    textRect=textSurf.get_rect()
    textRect.center = ( round(x+(w/2)), round(y+(h/2)) )
    screen.blit(textSurf, textRect)

def dodge(score,level):
	high=get_high_score()
	fnt = pygame.font.SysFont("comicsans", 20)
	txt = fnt.render("LEVEL : "+str(level), 1, red)
	screen.blit(txt, (5, 10))
	txt = fnt.render("SCORE : "+str(score), 1, (255,255,255))
	screen.blit(txt, (5, 30))
	txt = fnt.render("HIGH SCORE", 1, (255,255,255))
	screen.blit(txt, (707, 10))
	txt = fnt.render(str(high), 1, (255,255,255))
	screen.blit(txt, (707, 30))


def car(startx,starty,carno):
	a="image/Car"+str(carno)+".jpg"
	return pygame.image.load(a)


def crash(score):

	high=get_high_score()

	pygame.mixer.music.load('audio/crash1.mp3')
	pygame.mixer.music.play(1)

	fnt1 = pygame.font.SysFont("comicsans", 80)
	txt = fnt1.render(" GAME OVER ", 1, (0,0,0))
	screen.blit(txt, (215, 100))
	fnt = pygame.font.SysFont("comicsans", 20)
	txt = fnt.render("SCORE "+str(score), 1, (255,255,255))
	screen.blit(txt, (260, 160))
	if score>high:
		save_high_score(score)
		fnt2 = pygame.font.SysFont("comicsans", 40)
		txt = fnt2.render("CONGRATULATIONS", 1, red)
		screen.blit(txt, (270, 220))
		txt = fnt.render("YOU SET A NEW HIGH SCORE ", 1, (255,255,255))
		screen.blit(txt, (310, 250))
	high=get_high_score()
	txt = fnt.render("HIGH SCORE "+str(high), 1, (255,255,255))
	screen.blit(txt, (440, 160))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()

		button("RESTART",200,300,150,50,blue,light_blue,white,play)
		button("QUIT",450,300,150,50,blue,light_blue,white,quitgame)

		pygame.display.update()


def gameloop():

	pygame.mixer.music.load('audio/jazz.mp3')
	pygame.mixer.music.play(-1)

	global pause

	x=380
	y=465
	x_change=0
	y_change=0
	y2=7

	carno=random.randrange(1,6)
	startx = random.randrange(110,635)
	starty = -obs_height
	speed = 12

	level=1
	count=0
	score=0
	i=2


	crashed = False
	while not crashed:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change-=5
				if event.key == pygame.K_RIGHT:
					x_change+=5
				if event.key == pygame.K_UP:
					y_change-=3
				if event.key == pygame.K_DOWN:
					y_change+=3
				if event.key == pygame.K_p:
					pause = True
					paused()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change=0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change=0

		x+=x_change
		y+=y_change
		screen.fill(gray)

		rel_y=y2%side.get_rect().width
		screen.blit(side,(0,rel_y-side.get_rect().width))
		screen.blit(side,(700,rel_y-side.get_rect().width))
		if rel_y<800:
			screen.blit(side,(0,rel_y))
			screen.blit(side,(700,rel_y))
			#screen.blit(whi,(110,rel_y))
			#screen.blit(whi,(690,rel_y))
			screen.blit(yell,(405,rel_y+10))
			screen.blit(yell,(405,rel_y+110))
			screen.blit(yell,(405,rel_y+210))
			screen.blit(yell,(405,rel_y+310))
			screen.blit(yell,(405,rel_y+410))
			screen.blit(yell,(405,rel_y+510))

		y2+=speed
		screen.blit(whi,(110,0))
		screen.blit(whi,(690,0))
		screen.blit(img,(x,y))

		if (x>635 or x<110):
			crash(score)

		if y<5:
			y=5

		if y>475:
			y=475

		starty+=(speed//4)
		c=car(startx,starty,carno)
		screen.blit(c,(startx,starty))
		dodge(score,level)
	
		if starty > height:
			starty = -obs_height
			startx = random.randrange(110,635)
			carno=random.randrange(1,6)
			count+=1
			score+=1
			if count==(5*i):
				i+=1
				count=0
				level+=1
				speed+=6
				fnt2 = pygame.font.SysFont("comicsans", 60)
				txt = fnt2.render("LEVEL  "+str(level), 1, red)
				screen.blit(txt, (330, 50))
				pygame.display.update()
				time.sleep(1)


		if y < starty+obs_height and y > starty-125:
			if (x > startx and x < startx + obs_width) or (x+car_width >startx and x + car_width < (startx + obs_width)):
				crash(score)
		pygame.display.update()

def menu():
	front()

def paused():

	pygame.mixer.music.pause()

	fnt1 = pygame.font.SysFont("comicsans", 80)
	txt = fnt1.render(" PAUSED ", 1, (0,0,0))
	screen.blit(txt, (278, 200))

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()

		#screen.blit(back,(0,0))

		button("CONTINUE",127,300,150,50,blue,light_blue,white,unpause)
		button("QUIT",527,300,150,50,blue,light_blue,white,quitgame)
		button("RESTART",327,300,150,50,blue,light_blue,white,play)
		pygame.display.update()

def quitgame():
	pygame.quit()
	quit()
	sys.exit()

def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause = False

def play():
	countdown()

def intro():
	introloop()

def qui():
	pygame.quit()
	quit()
	sys.exit()

def introloop():
	introduction=True
	while introduction:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()
		screen.blit(back1,(0,0))
		fnt1 = pygame.font.SysFont("comicsans", 60)
		fnt = pygame.font.SysFont("comicsans", 30)
		fnt2 = pygame.font.SysFont("comicsans", 40)
		txt = fnt1.render(" CONTROLS ", 1, red)
		screen.blit(txt, (273, 100))
		screen.blit(left,(290,330))
		screen.blit(down,(370,330))
		screen.blit(right,(450,330))
		screen.blit(up,(370,250))
		txt = fnt.render("LEFT", 1, (0,0,0))
		screen.blit(txt, (235, 350))
		txt = fnt.render("ACCELERATOR", 1, (0,0,0))
		screen.blit(txt, (325, 230))
		txt = fnt.render("RIGHT", 1, (0,0,0))
		screen.blit(txt, (525, 350))
		txt = fnt.render("BRAKE", 1, (0,0,0))
		screen.blit(txt, (365, 400))
		screen.blit(p,(320,470))
		txt = fnt.render("PAUSE", 1, (0,0,0))
		screen.blit(txt, (375, 485))
		button("BACK",630,25,150,50,blue,light_blue,white,menu)
		pygame.display.update()


def front():
	fro = True
	while fro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()

		screen.blit(back,(0,0))
		fnt1 = pygame.font.SysFont("comicsans", 80)
		txt = fnt1.render(" TURBO ", 1, red)
		screen.blit(txt, (273, 130))
		button("NEW GAME",115,300,150,50,blue,light_blue,white,play)
		button("QUIT",515,300,150,50,blue,light_blue,white,qui)
		button("INSTRUCTIONS",315,300,150,50,blue,light_blue,white,intro)
		pygame.display.update()


front()

pygame.quit()
quit()