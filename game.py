import os, pygame, math, random
from random import randint
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 300
		self.dx = randint(3,5)
		self.dy = randint(0,2)

	def update(self):
		self.rect.x += self.dx
		self.rect.y += self.dy
		if self.rect.y > 590 or self.rect.y < 0:
			self.dy = self.dy * -1
		
	def hitPad(self):
		self.dx = self.dx * -1


class Pad(pygame.sprite.Sprite):
	def __init__(self, playernumber, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 200])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.active = 0
		if playernumber == 1:
			self.rect.x = 0
		else:
			self.rect.x = 790
		self.rect.y = 300

	def move(self, direction):
		if direction == 'up' and self.rect.y > 0:
			self.rect.y -= 50
		if direction == 'down' and self.rect.y < 400:
			self.rect.y += 50

class Game(pygame.sprite.Sprite):
	def __init__(self):
		self.score = [0,0]
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([100,50])
		self.rect = self.image.get_rect()
			
def main():
	pygame.init()
	size = [800, 600]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Pong Yourself")
	pygame.mouse.set_visible(0)
	background = pygame.Surface(screen.get_size())
	
	if pygame.font:
		font = pygame.font.Font(None, 30)

	game = Game()

	ball = Ball()
	balls = pygame.sprite.Group()
	balls.add(ball)
	
	pad1 = Pad(1, RED)
	pad2 = Pad(2, WHITE)

	allsprites = pygame.sprite.RenderPlain((balls, pad1, pad2))

	clock = pygame.time.Clock()

	while 1:
			
		background.fill(BLACK)

		text = font.render("Player Red: "+str(game.score[0]), True, WHITE)
		background.blit(text, (150,0))

		text = font.render("Player White: "+str(game.score[1]), True, WHITE)
		background.blit(text, (500,0))
		

		if ball.rect.x < 0:
			game.score[1] += 1
			ball.__init__()
		if ball.rect.x > 800:
			game.score[0] += 1
			ball.__init__()

		if ball.dx > 0:
			pad2.active = 1
			pad1.active = 0
			if pygame.sprite.spritecollide(pad2, balls, False):
				ball.hitPad()
		else:
			pad1.active = 1
			pad2.active = 0
			if pygame.sprite.spritecollide(pad1, balls, False):
				ball.hitPad()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type == KEYDOWN and event.key == K_UP:
				if pad1.active == 1:
					pad1.move('up')
				else:
					pad2.move('up')
			elif event.type == KEYDOWN and event.key == K_DOWN:
				if pad1.active == 1:
					pad1.move('down')
				else:
					pad2.move('down')
							
		clock.tick(60)
		balls.update()
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()