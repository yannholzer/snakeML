import pygame as pg
from settings import *
from sprites import *


class Game:
	def __init__(self):
		# init the game window, etc
		pg.init()
		self.win = pg.display.set_mode(SCREEN_SIZE) # init "win" window
		pg.display.set_caption(TITLE)  # set caption to window
		self.clock = pg.time.Clock() # define clock
		self.running = True # running variable for game loop

		self.counter = 0
		self.update_sprites = False

		self.score = 0



	def new(self):
		# start a new game
		# init sprites
		self.snake = Snake(self)
		self.food = Food(self)
		self.reward = 0
		self.run()


	def run(self):
		# Game Loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS) #time the loop with FPS value
			self.events()
			self.update()
			self.draw()
		self.running = False

	def update(self):
		# Game Loop - update
		self.counter += 1
		self.snake.update() # update all sprites group

		self.get_states()
		
		if self.counter == FPS/SNAKE_SPEED:
			self.counter = 0
			self.snake.going_direction = self.snake.chosen_direction
			if self.snake.body[0] + self.snake.going_direction*10 == self.food.pos:
				self.reward += 10
				self.snake.body.insert(0, self.food.pos)
				self.food.set_location()
				self.score += 10
				print("new score:", self.score)

			else:
				for i in range(len(self.snake.body)-1, 0, -1):
					self.snake.body[i] = self.snake.body[i-1].copy()
				self.snake.body[0] += self.snake.going_direction*10
				
				self.check_collision()


	def check_collision(self):
		for bodies in self.snake.body[1:]:
			if self.snake.body[0] == bodies:
				self.game_over()
		if self.snake.body[0].x < 0 or self.snake.body[0].y < 0:
			self.game_over()
		if self.snake.body[0].x > SCREEN_SIZE[0] - 10 or self.snake.body[0].y > SCREEN_SIZE[1] - 10:
			self.game_over()


	def get_states(self):
		# get food direction
		# danger up - down - left - right
		# food up - down - left - right 
		# going dir up - down - left - right
		state = 12*[0]

		danger = {
			"left": False,
			"right": False,
			"up": False,
			"down": False
		}
  
		food = {
			"left": False,
			"right": False,
			"up": False,
			"down": False
		}
  
		direction = {
			"left": False,
			"right": False,
			"up": False,
			"down": False
		}


		danger["right"] = self.snake.body[0].x + 10 > SCREEN_SIZE[0] -10
		danger["down"] = self.snake.body[0].y + 10 > SCREEN_SIZE[1] -10
		danger["left"] = self.snake.body[0].x - 10 < 0
		danger["up"] = self.snake.body[0].y - 10 < 0
			
		food["right"] = self.snake.body[0].x  < self.food.pos.x
		food["down"] = self.snake.body[0].y  < self.food.pos.y
		food["left"] = self.snake.body[0].x > self.food.pos.x
		food["up"] = self.snake.body[0].y  > self.food.pos.y
  
		direction["right"] = self.snake.going_direction.x  > 0
		direction["down"] = self.snake.going_direction.y  > 0
		direction["left"] = self.snake.going_direction.x  < 0
		direction["up"] = self.snake.going_direction.y < 0

		
		state[0:4] = list(danger.items())
		state[4:8] = list(food.items())
		state[8:12] = list(direction.items())
  

		# get danger ahead





	def game_over(self):
		self.reward -= 10
		print("GAME OVER")
		pg.time.wait(2000)
		self.playing = False

		

	def events(self):
		# Game Loop - events
		for event in pg.event.get():
			if event.type == pg.QUIT: # check for closing window
				self.playing = False # stop the run loop
				self.running = False # stop the main loop
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE: # check for esc key press
					self.playing = False
					self.running = False


	def draw(self):
		# Game Loop - draw
		self.win.fill(COLORS["BLACK"]) # fill the win with black
		
		#self.food.draw(self.win) # draw all sprites group
		pg.draw.rect(self.win, COLORS["CYAN"], self.food.rect)
		for b in self.snake.body:			
			pg.draw.rect(self.win, COLORS["WHITE"], pg.Rect((b), (10,10)))


		pg.display.flip() # double buffering


			


g = Game()
#g.show_start_win()
while g.running :
	g.new()
	#g.show_gameover_win()

pg.quit()


