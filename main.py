import random
import pygame

pygame.mixer.init()
background_image = pygame.image.load("final_screen.jpeg")
background_image = pygame.transform.scale(background_image, (800, 600))
background_rect = background_image.get_rect()
angle = 0
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)


bounce_sound = pygame.mixer.Sound("tennis_bounce.ogg")
background_music = pygame.mixer.Sound("bg2.mp3")
pygame.mixer.music.load("bg2.mp3")
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            running = False

# initial position and velocity of the ball
x = window_size[0] // 2
y = window_size[1] // 2
vx = random.uniform(-150, 150)
vy = random.uniform(-150, 150)

ball_size = 10

clock = pygame.time.Clock()
max_velocity = 200
click_count = 0
click_time = pygame.time.get_ticks()
bounce_count = 0

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            current_time = pygame.time.get_ticks()
            if current_time - click_time < 300:
                click_count += 1
            else:
                click_count = 1
            click_time = current_time

            if event.button == 1: # Left mouse button
                vx *= 0.75
                vy *= 0.75
            elif event.button == 3: # Right mouse button
                vx *= 1.25
                vy *= 1.25

    # Clear the screen
    screen.blit(background_image, background_rect)

    # Increase the angle for the next iteration
    angle += 1

    # Update the position of the ball based on its velocity
    x += vx * clock.get_time() / 1000
    y += vy * clock.get_time() / 1000


    # Check if the ball hits any of the borders
    if x < 0 or x > window_size[0]:
        vx = -vx * 1.05
        pygame.mixer.Sound.play(bounce_sound)
        if x < 0:
            screen.fill((0, 255, 0), (0, 0, 10, window_size[1]))
        else:
            screen.fill((0, 255, 0), (window_size[0] - 10, 0, 10, window_size[1]))
        bounce_count += 1
    if y < 0 or y > window_size[1]:
        vy = -vy * 1.05
        pygame.mixer.Sound.play(bounce_sound)
        if y < 0:
            screen.fill((255, 255, 255), (0, 0, window_size[0], 10))
        else:
            screen.fill((255, 255, 255), (0, window_size[1] - 10, window_size[0], 10))
        bounce_count += 1

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 240), (int(x), int(y)), ball_size)

    # Check if the ball has bounced 1000 times
    if bounce_count >= 100:
        # Stop the game loop
        running = False


    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(60)

# Close the window
pygame.quit()