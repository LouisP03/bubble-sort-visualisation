# Sorting Algorithm Visualiser
import time, random, pygame, sys, math
try:
	import configparser
except:
	from six.moves import configparser

#config stuff
config = configparser.ConfigParser()
config.read("config.ini")

pygame.init()
clock = pygame.time.Clock()
FPS = int(config['default']['framerate'])
universal_delay = int(config['default']['universal_delay'])

screen_width, screen_height = int(config['default']['screen_width']), int(config['default']['screen_height'])
screen = pygame.display.set_mode((screen_width,screen_height))
bg_colour = (int(config['default']['background_colour_R']), int(config['default']['background_colour_G']), int(config['default']['background_colour_B']))
wpb = int(config['default']['bar_width']) #width plus border
light_grey = (200,200,200)
black = (0,0,0)
red = (255,0,0)
conf_colour = (int(config['default']['bar_colour_R']), int(config['default']['bar_colour_G']), int(config['default']['bar_colour_B']))

def randomise(length):
	array = [None for index in range(length)]
	for i in range(0, len(array)):
		array[i] = random.randint(1, int(screen_height)-int(math.floor(screen_height*0.10)))
	return array

def createRects(array):
	global screen_width,screen_height,black,red
	global conf_colour
	on_screen = [pygame.Rect(i*wpb, 0, (wpb-1), array[i]) for i in range(0, len(array)-1)]
	for val in range(0, len(on_screen)):
		pygame.draw.rect(screen, conf_colour, on_screen[val])
		pygame.display.flip()
	pygame.time.delay(int(config['default']['first_delay']))

	return array, on_screen
	
def bubble(arrs):
	global black, conf_colour, red, wpb, universal_delay
	array, on_screen = arrs[0], arrs[1]
	n = len(array)
	print(n)
	print(on_screen)
	swapped = True
	while swapped:
		swapped = False
		for loop in range(1, n-1):
			if array[loop-1] > array[loop]:
				array[loop-1], array[loop] = array[loop], array[loop-1]
				pygame.draw.rect(screen, black, on_screen[loop-1])
				pygame.draw.rect(screen, black, on_screen[loop])
				on_screen[loop-1], on_screen[loop] = on_screen[loop], on_screen[loop-1]
				on_screen[loop].x += wpb
				on_screen[loop-1].x -= wpb
				pygame.draw.rect(screen, conf_colour, on_screen[loop-1])
				pygame.draw.rect(screen, conf_colour, on_screen[loop])
				pygame.display.flip()
				pygame.time.delay(universal_delay)
				swapped = True
	return array



#print(bubble([4,2,5,1,7,4,8]))
"""on_screen = [pygame.Rect(i*10, i*10, 5, 5) for i in range(0, 6)]
for val in range(0, len(on_screen)-1):
	pygame.draw.rect(screen, conf_colour, on_screen[val])

"""
def start():
	randomised = randomise(250)
	print(randomised)
	arr = createRects(randomised)
	print(bubble(arr))
	#print(createRects(bubble(arr)))

start()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSLASH:
				pygame.quit()
				sys.exit()

	#screen.fill(bg_colour)
	#start()

	pygame.display.flip()
	clock.tick(FPS)
