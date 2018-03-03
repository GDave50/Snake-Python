import pygame
import __init__ as glo
import game

# handles the events for the window
def check_events(game_instance):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				game_instance.change_snake_dir(glo.Direction.UP)
			elif event.key == pygame.K_DOWN:
				game_instance.change_snake_dir(glo.Direction.DOWN)
			elif event.key == pygame.K_LEFT:
				game_instance.change_snake_dir(glo.Direction.LEFT)
			elif event.key == pygame.K_RIGHT:
				game_instance.change_snake_dir(glo.Direction.RIGHT)
	
	return True

# program entry point
def main():
	pygame.init()
	pygame.mixer.init()
	# make the window
	screen = pygame.display.set_mode((glo.WINDOW_SIZE, glo.WINDOW_SIZE))
	# set the title of the window
	pygame.display.set_caption(glo.WINDOW_TITLE)
	# initialize font
	global FONT
	glo.FONT = pygame.font.SysFont(glo.FONT_NAME, glo.FONT_SIZE)
	
	# create the sounds
	global EAT_SOUND
	global DIE_SOUND
	glo.EAT_SOUND = pygame.mixer.Sound('res/sounds/eat.wav')
	glo.DIE_SOUND = pygame.mixer.Sound('res/sounds/die.wav')
	
	# make the game clock
	clock = pygame.time.Clock()
	
	game_instance = game.Game()
	should_run = True
	
	while should_run:
		# check events
		should_run = check_events(game_instance)
		
		# do game logic
		game_over = game_instance.game_logic()
		if game_over:
			game_over = False
			game_instance.reset()
		
		# clear screen in preparation for drawing
		screen.fill(glo.BACKGROUND_COLOR)
		# draw the game
		game_instance.draw(screen)
		# show the new drawing
		pygame.display.flip()
		
		# update game clock
		clock.tick(glo.WINDOW_FPS)
	
	# quit the game when the loop is over
	pygame.quit()

if __name__ == '__main__':
	main()