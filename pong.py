import tkinter as tk
import random

# Game configurations
WIDTH = 800
HEIGHT = 600
BALL_SPEED = 3
PADDLE_SPEED = 6
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# Ball movement directions
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Paddle positions
left_paddle_y = HEIGHT // 2
right_paddle_y = HEIGHT // 2

# Scores
left_score = 0
right_score = 0

# Function to move the left paddle up
def left_paddle_up(event):
    global left_paddle_y
    left_paddle_y -= PADDLE_SPEED
    canvas.coords(left_paddle, 10, left_paddle_y, 10 + PADDLE_WIDTH, left_paddle_y + PADDLE_HEIGHT)

# Function to move the left paddle down
def left_paddle_down(event):
    global left_paddle_y
    left_paddle_y += PADDLE_SPEED
    canvas.coords(left_paddle, 10, left_paddle_y, 10 + PADDLE_WIDTH, left_paddle_y + PADDLE_HEIGHT)

# Function to move the right paddle up
def right_paddle_up(event):
    global right_paddle_y
    right_paddle_y -= PADDLE_SPEED
    canvas.coords(right_paddle, WIDTH - 10 - PADDLE_WIDTH, right_paddle_y, WIDTH - 10, right_paddle_y + PADDLE_HEIGHT)

# Function to move the right paddle down
def right_paddle_down(event):
    global right_paddle_y
    right_paddle_y += PADDLE_SPEED
    canvas.coords(right_paddle, WIDTH - 10 - PADDLE_WIDTH, right_paddle_y, WIDTH - 10, right_paddle_y + PADDLE_HEIGHT)

# Function to update scores and reset the ball
def update_score():
    global left_score, right_score
    ball_coords = canvas.coords(ball)
    ball_x = ball_coords[0]

    # Check if the ball is out of bounds on the left or right side
    if ball_x <= 0:
        right_score += 1
        reset_ball()
    elif ball_x >= WIDTH - 20:
        left_score += 1
        reset_ball()

    # Update the score display
    score_display.config(text=f"Left Player: {left_score}   Right Player: {right_score}")

    # Schedule next update
    win.after(20, update_score)

# Game loop
def update_game():
    global ball_dx, ball_dy
    # Move the ball
    ball_coords = canvas.coords(ball)
    ball_x, ball_y = ball_coords[0], ball_coords[1]

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - 20:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ball_x <= 25 and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_dx = BALL_SPEED
    elif ball_x >= WIDTH - 45 and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_dx = -BALL_SPEED

    # Move the ball
    canvas.move(ball, ball_dx, ball_dy)

    # Schedule next update
    win.after(20, update_game)

# Function to reset the ball to the center
def reset_ball():
    global ball_dx, ball_dy
    canvas.coords(ball, WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10)
    ball_dx = BALL_SPEED if random.choice([True, False]) else -BALL_SPEED
    ball_dy = BALL_SPEED if random.choice([True, False]) else -BALL_SPEED

# Main function to set up the game
def main():
    global canvas, left_paddle, right_paddle, ball, win, score_display

    # Set up the game window
    win = tk.Tk()
    win.title("Pong Game")
    win.geometry(f"{WIDTH}x{HEIGHT}")

    # Create the canvas
    canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    # Create the left paddle
    left_paddle = canvas.create_rectangle(10, left_paddle_y, 10 + PADDLE_WIDTH, left_paddle_y + PADDLE_HEIGHT, fill="white")

    # Create the right paddle
    right_paddle = canvas.create_rectangle(WIDTH - 10 - PADDLE_WIDTH, right_paddle_y, WIDTH - 10, right_paddle_y + PADDLE_HEIGHT, fill="white")

    # Create the ball
    ball = canvas.create_oval(WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10, fill="white")

    # Create the score display
    score_display = tk.Label(win, text="Left Player: 0   Right Player: 0", font=("Courier", 24), fg="white", bg="black")
    score_display.pack()

    # Bind paddle movement to keyboard events
    win.bind("<w>", left_paddle_up)
    win.bind("<s>", left_paddle_down)
    win.bind("<Up>", right_paddle_up)
    win.bind("<Down>", right_paddle_down)

    # Start the game loop
    update_game()
    update_score()

    # Run the game
    win.mainloop()

if __name__ == "__main__":
    main()
