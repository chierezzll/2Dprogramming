from pico2d import *

 

def handle_events():

	global running, dx, x, y

	events = get_events()

	for e in events:

		if e.type == SDL_QUIT:

			running = False

		elif e.type == SDL_KEYDOWN:

			if e.key == SDLK_ESCAPE:

				running = False

			elif e.key == SDLK_LEFT:

				dx = -1

			elif e.key == SDLK_RIGHT:

				dx = 1 

			elif e.key == SDLK_SPACE:

				dx = 0

		elif e.type == SDL_KEYUP:

			if e.key == SDLK_RIGHT:

				dx = 0 

			elif e.key == SDLK_LEFT:

				dx = 0

		elif e.type == SDL_MOUSEMOTION:

			x, y = e.x, get_canvas_height() - e.y - 1

 

 

 

 

open_canvas()

 

x, y = 400, 85

dx = 0

running = True

fidx = 0

grass = load_image('grass.png')

character = load_image('run_animation.png')

 

while running and x < 800:

	clear_canvas()

	grass.draw(400, 30)

	character.clip_draw(fidx*100, 0 , 100, 100, x, y)

	update_canvas()

 

	handle_events()

	

	

	fidx =(fidx + 1) % 8

	x += dx 

	delay(0.01)

 

 

 

close_canvas()