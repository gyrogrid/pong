import os, sys, game, pygame
from pygame.locals import *

BLACK = (0,0,0)

def load_image(name, colorkey=None):
		fullname = os.path.join('data', name)
		image = pygame.image.load(fullname)
		image = image.convert()
		return image, image.get_rect()

class Start(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([100,50])
		self.image, self.rect = load_image('start.png')
		self.rect.x = 300
		self.rect.y = 30

class Quit(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([100,50])
		self.image, self.rect = load_image('quit.png')
		self.rect.x = 300
		self.rect.y = 100

class Arrow(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x = 450
		self.rect.y = 100

	def move(self, direction):
		if direction == 'up':
			if self.rect.y == 100:
				self.rect.y = 30
		if direction == 'down':
			 if self.rect.y == 30:
			 	self.rect.y = 100

	def select(self):
		if self.rect.y == 30:
			game.main()
		if self.rect.y == 100:
			pygame.display.quit()
			sys.exit()                        


def main():
	pygame.init()
	size = [800, 600]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Pong Yourself")
	pygame.mouse.set_visible(0)
	background = pygame.Surface(screen.get_size())

	start = Start()
	quit = Quit()
	arrow = Arrow()

	allsprites = pygame.sprite.RenderPlain((start, quit, arrow))
	clock = pygame.time.Clock()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type == KEYDOWN and event.key == K_DOWN:
				arrow.move('down')
			elif event.type == KEYDOWN and event.key == K_UP:
				arrow.move('up')
			elif event.type == KEYDOWN and event.key == K_RETURN:
				arrow.select()

		clock.tick(60)
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()