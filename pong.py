import pygame
import sys
from pygame.locals import *

# Refer to http://www.pygame.org/docs/

# # of Frames Per Second
FPS = 200
# Dimensions of the Pong window
SquareSize = 600
Height = SquareSize
Width = SquareSize
# Thickness of Bar in program
PaddleThickness = 10
# Length of Paddle
# Edge of playable screen
Edge = 2 * PaddleThickness
PaddleLength = .2 * (Width - 2 * Edge)
# Distance the paddle is away from the Wall
PaddleDistance = 20
# Ball dimensions
BallWidth = 10
BallHeight = 10

# COLORS !!
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,200,255)
def DrawArena():
	# Black Background
	Display.fill(Black)
	# Format pygame.draw.rect(Surface, color, Rect, width=0) -> Rect
	# Drawing the actual arena/ Rectangle
	outline = pygame.Rect(0,0,Width,Height)
	pygame.draw.rect(Display, Blue , outline, Edge)

def DrawPaddle(PaddleController):

	# We check for legal actions such as moving to an invalid pixel location
	if( PaddleController.top < Edge):
		PaddleController.top = Edge
	elif( PaddleController.bottom > Height - Edge ):
		PaddleController.bottom = Height - Edge
	# once checked for illegal actions, draw the paddle
	pygame.draw.rect(Display,Red,PaddleController)
def DrawBall(BallController):
	# if( BallController.top < Edge):
	# 	BallController.top = Edge
	# elif( BallController.bottom > Height - Edge):
	# 	BallController.bottom = Edge
	pygame.draw.rect(Display, Red, BallController)

def MoveBall(BallController, BallSpeedX,BallSpeedY):
	# Move the Ball
	BallController.x += BallSpeedX
	BallController.y += BallSpeedY
	return BallController
def Collision_Detection_Paddle(BallController, PaddleController, BallSpeedX):
	if BallSpeedX > 0 and PaddleController.left== BallController.right and PaddleController.top < BallController.top and PaddleController.bottom > BallController.bottom:
		return -1
	else:
		return 1
	return BallSpeedX

def Collision_Detection(BallController, BallSpeedX, BallSpeedY):
	if(BallController.top == Edge/2 or BallController.bottom == Height - Edge/2):
		BallSpeedY = -1 * BallSpeedY
	if(BallController.left == Edge/2 or BallController.right == Width - Edge/2):
		BallSpeedX = -1 * BallSpeedX
	return BallSpeedX, BallSpeedY

def main():
	# initialize pygame:
	pygame.init()

	# To quit, use  pygame.quit()
	global Display
	
	# how fast the game will run (controlled through FPS variable)
	FPSClock = pygame.time.Clock()
	
	# this will create a 600 x 600 display
	Display = pygame.display.set_mode((Height,Width))
	pygame.display.set_caption('MP4.1 Pong')

	# Initial Ball Position
	BallX = int(( Width - PaddleThickness) / 3)
	BallY = int((Height - PaddleThickness) / 2)

	# initial Paddle positions
	Paddle_PosY = int((Height - PaddleLength) / 2)
	Paddle_PosX = int((Width - PaddleDistance - PaddleThickness))
	# creating Paddle and the Ball
	# Format : pygame.Rect(X co-ordinate, Y co-ordinate, Width of Rectangle, Length of Rectangle)
	PaddleController = pygame.Rect(Paddle_PosX, Paddle_PosY, PaddleThickness, PaddleLength)
	#PaddleController2 = pygame.Rect(PaddleDistance, Paddle_Posy, PaddleThickness, PaddleLength )
	# ball is treated as a rectangle for simplicity
	BallController = pygame.Rect(BallX, BallY, BallWidth, BallHeight )

	BallSpeedX = -1
	BallSpeedY = -1
	# Drawing initial Positions of the Ball and Paddle and arena
	DrawArena()
	DrawPaddle(PaddleController)
	# #DrawPaddle(PaddleController2)
	DrawBall(BallController)
	# Game Loop
	Game_on = True
	while Game_on:
		# We will give our program the ability to quit
		for event in pygame.event.get():
			if(event.type == QUIT):
				pygame.quit()
				sys.exit()
			# keys = pygame.key.get_pressed()
			# if( keys[K_LEFT]):
			# 	PaddleController.y += 25
			# if( keys[K_RIGHT]):
			# 	PaddleController.y -= 25
			elif(event.type == KEYDOWN):
				if(event.key == pygame.K_LEFT):
					if(PaddleController.bottom <= Height - Edge):
						PaddleController.y += 50
				elif( event.key ==pygame.K_RIGHT):
					if(PaddleController.top >= Edge):
						PaddleController.y -= 50
						
			
		# ReDrawing Updated scene
		DrawArena()
		DrawPaddle(PaddleController)
		# #DrawPaddle(PaddleController2)
		DrawBall(BallController)
		# Update Ball Position
		BallController = MoveBall(BallController, BallSpeedX,BallSpeedY)
		# checking for collisions with walls
		BallSpeedX , BallSpeedY = Collision_Detection(BallController, BallSpeedX, BallSpeedY)
		# Checking for collisions with paddle
		BallSpeedX = BallSpeedX * Collision_Detection_Paddle(BallController, PaddleController, BallSpeedX)
		# this will update the screen
		pygame.display.update()
		# use our predefined FPS instead of max FPS
		FPSClock.tick(FPS)
if __name__=='__main__':
	main()
