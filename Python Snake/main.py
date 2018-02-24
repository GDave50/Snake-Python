import pygame
import global_consts as glo
import game

def main():
	pygame.init()
	
	# make the window
	screen = pygame.display.set_mode((glo.WINDOW_SIZE, glo.WINDOW_SIZE))
	
	# set the title of the window
	pygame.display.set_caption(glo.WINDOW_TITLE)
	
	# make the game clock
	clock = pygame.time.Clock()
	
	game_instance = game.Game()
	should_run = True
	
	while should_run:
		# check events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				should_run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					game_instance.change_snake_dir(glo.Direction.UP)
				elif event.key == pygame.K_DOWN:
					game_instance.change_snake_dir(glo.Direction.DOWN)
				elif event.key == pygame.K_LEFT:
					game_instance.change_snake_dir(glo.Direction.LEFT)
				elif event.key == pygame.K_RIGHT:
					game_instance.change_snake_dir(glo.Direction.RIGHT)
		
		# game logic
		game_over = game_instance.game_logic()
		
		if game_over:
			should_run = False
			break
		
		# clear screen in preparation for drawing
		screen.fill(glo.BACKGROUND_COLOR)
		
		# draw the game
		game_instance.draw(screen)
		
		# show the new drawing
		pygame.display.flip()
		
		# update game clock
		clock.tick(glo.WINDOW_FPS)
	
	pygame.quit()

if __name__ == '__main__':
	main()