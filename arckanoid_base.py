import pygame  
import random 
pygame.init() 
 
W, H = 800, 600 
FPS = 60 
 
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE) 
clock = pygame.time.Clock() 
done = False 
bg = (255, 192, 203) 
 
# Section #2. Adding objects of a ball and a paddle 
paddleW = 200 
paddleH = 25 
paddleSpeed = 20 
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH) 
 
# Ball 
ballRadius = 20 
ballSpeed = 6 
ballSpeedIncrease = 0.05  # Speed increase per frame
ball_rect = int(ballRadius * 2 ** 0.5) 
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect) 
dx, dy = 1, -1 

# Paddle shrink with time
paddleShrinkRate = 0.05  # Rate of paddle width reduction per frame

# Bricks with random colors and types
brickW, brickH = 75, 25
bricks = []
brick_colors = []
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
for row in range(3):  # Three rows of bricks
    for col in range(10):
        if row == 0 and col % 3 == 0:  # Create some unbreakable bricks in the first row
            brick = pygame.Rect(col * (brickW + 10) + 35, 100 + row * (brickH + 10), brickW, brickH)
            bricks.append((brick, True))  # True indicates unbreakable brick
        else:
            brick = pygame.Rect(col * (brickW + 10) + 35, 100 + row * (brickH + 10), brickW, brickH)
            bricks.append((brick, False))  # False indicates breakable brick
        brick_colors.append(random.choice(colors))

# Bonus bricks with perks
bonusBricks = []
bonusColors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Game over 
font = pygame.font.SysFont('comicsansms', 40) 
text = font.render('Game Over', True, (255, 255, 255)) 
textRect = text.get_rect() 
textRect.center = (W // 2, H // 2) 

# Game loop
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    screen.fill(bg) 
     
    pygame.draw.rect(screen, pygame.Color(234, 250, 177), paddle) 
    pygame.draw.circle(screen, pygame.Color(250, 241, 157), ball.center, ballRadius) 

    # Draw bricks with their random colors
    for i, (brick, unbreakable) in enumerate(bricks):
        pygame.draw.rect(screen, brick_colors[i], brick)
     
    # Paddle Control with shrinking
    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT] and paddle.left > 0: 
        paddle.left -= paddleSpeed 
    if key[pygame.K_RIGHT] and paddle.right < W: 
        paddle.right += paddleSpeed 
    paddleW -= paddleShrinkRate
    paddle.width = max(int(paddleW), 1)  # Ensure paddle width doesn't go below 1 pixel

    # Ball movement with speed increase
    ball.x += ballSpeed * dx 
    ball.y += ballSpeed * dy 
    ballSpeed += ballSpeedIncrease

    # Collision left or right  
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius: 
        dx = -dx 
    # Collision TOP 
    if ball.centery < ballRadius + 50:  
        dy = -dy 
    # Collision with paddle 
    if ball.colliderect(paddle) and dy > 0: 
        dy = -dy 

    # Collision with bricks
    for i, (brick, unbreakable) in enumerate(bricks[:]):
        if ball.colliderect(brick):
            if not unbreakable:
                dy = -dy
                bricks.pop(i)
                brick_colors.pop(i)
                # Add a bonus brick randomly after breaking a regular brick
                if random.random() < 0.1:  # 10% chance of a bonus brick appearing
                    bonusBrick = pygame.Rect(brick.left, brick.top, brickW, brickH)
                    bonusBricks.append((bonusBrick, random.choice(bonusColors)))
            else:
                dx = -dx
                dy = -dy
    
    # Check for game over
    if ball.y > H or ball.x > W: 
        screen.fill((0, 0, 0)) 
        screen.blit(text, textRect) 
 
    pygame.display.update() 
    clock.tick(FPS)