import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN =(0,255,0)
RED = (255,0,0)


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():						   #initializes a board with zeros using NumPy
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):	   #places a piece on the board at a specified row and column
	board[row][col] = piece

def is_valid_location(board, col):		   #checks if a specific column in the board has space for an additional piece.determines if a move is legal
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):			   #finds the next available row in the specified column from bottom to top
		if board[r][col] == 0:
			return r


def print_board(board):					   #prints the board with rows flipped vertically to align with standard game visualization
	print(np.flip(board, 0))

def winning_move(board, piece):            #checks for horizontal, vertical, positively sloped diagonal, and negatively sloped diagonal win conditions
	
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):		   #This loop iterates through each column (c) of the board up to COLUMN_COUNT - 3
		for r in range(ROW_COUNT):	   #iterates through each row (r) of the board for the current column c
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
						#it checks:
						#board[r][c] == piece: Piece at current position.
						#board[r][c+1] == piece: Piece one position to the right.
						#board[r][c+2] == piece: Piece two positions to the right.
						#board[r][c+3] == piece: Piece three positions to the right.
				return True
	

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):		    #This loop iterates through each column (c) 
		for r in range(ROW_COUNT-3):		#iterates through each row (r) of the board for the current column c, but it stops at ROW_COUNT - 3
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
						#Specifically, it checks:
						#board[r][c] == piece: Piece at the current position.
						#board[r+1][c] == piece: Piece one row below.
						#board[r+2][c] == piece: Piece two rows below.
						#board[r+3][c] == piece: Piece three rows below.			
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):			#This loop iterates through each column (c), but it stops at COLUMN_COUNT - 3
		for r in range(ROW_COUNT-3):		#This loop iterates through each row (r), but it stops at ROW_COUNT - 3
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
						#Specifically, it checks:
						#board[r][c] == piece: Piece at the current position.
						#board[r+1][c+1] == piece: Piece one position diagonally below and to the right.
						#board[r+2][c+2] == piece: Piece two positions diagonally below and to the right.
						#board[r+3][c+3] == piece: Piece three positions diagonally below and to the right.
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):			#This loop iterates through each column (c), but it stops at COLUMN_COUNT - 3
		for r in range(3, ROW_COUNT):		#This loop iterates through each row (r), starting from r = 3.
							#This ensures that the loop starts from a row where there are enough rows above (r-1, r-2, r-3) to potentially form a sequence of four pieces diagonally.
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
					   #Specifically, it checks:
					   #board[r][c] == piece: Piece at the current position.
					   #board[r-1][c+1] == piece: Piece one position diagonally above and to the right.
					   #board[r-2][c+2] == piece: Piece two positions diagonally above and to the right.
					   #board[r-3][c+3] == piece: Piece three positions diagonally above and to the right.
				return True

def draw_board(board):			   #drawing a Connect Four game board using the Pygame
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))		
						#draws a rectangle representing a grid square on the screen.
						#screen: The Pygame surface to draw on. BLUE: A color constant
						#Defines the rectangle's position and size based on the current column and row, scaled by SQUARESIZE.
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
						#draws a black circle in the center of the grid square.
						#Coordinates of the circle's center, calculated to be in the middle of the grid square.
						#RADIUS: The radius of the circle, defining its size.
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
						#draws a red circle, if player 1's piece is present at position (r, c).
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
						#draws a yellow circle, if player 2's piece is present at position (r, c).
						#The coordinates are used to position the circle based on the column c and row r of the board.
	pygame.display.update()
						#Finally, pygame.display.update() refreshes the Pygame display to show the updated board with all the grid squares and player pieces.


board = create_board()   #creates the game board
print_board(board)
game_over = False        #track whether the game is over
turn = 0                 #track of the current player's turn

pygame.init()

SQUARESIZE = 100         #size of each square in the game grid

width = COLUMN_COUNT * SQUARESIZE       #Calculates the width of the game window based on the number of columns and the size of each square
height = (ROW_COUNT+1) * SQUARESIZE     #Calculates the height of the game window. It adds one extra row to leave space for the piece drop area.

size = (width, height)                  #overall size of the game window as a tuple

RADIUS = int(SQUARESIZE/2 - 5)          #represent the pieces in the game

screen = pygame.display.set_mode(size)  #sets up the game window with the dimensions specified by size
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:           #The main loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#Mouse Motion Event
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		#Mouse Button Down Event
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, GREEN)
						screen.blit(label, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True

			print_board(board)
			draw_board(board)

			#Switch Turn between 0 and 1
			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)
