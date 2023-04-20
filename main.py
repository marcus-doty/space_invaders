import random
import math
import pygame
import random
from pygame import mixer

# Initialize the pygame
pygame.init()
# Create a screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Background
background = pygame.image.load('kitt.jpg')

# Background sound
mixer.music.load('heartlazer.mp3')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-rocket.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Alien
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 6
for i in range(num_of_aliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(50, 150))
    alienX_change.append(0.5)
    alienY_change.append(40)

# Heart
# Ready - You can't see the heart on the screen
# Fire - the heart is moving
heartImg = pygame.image.load('heart.png')
heartX = 0
heartY = 480
heartX_change = 0
heartY_change = 5
heart_state = "ready"

# Game start text



# Score
score_value = 0
font = pygame.font.Font('Lalezar-Regular.ttf', 32)
textX = 10
textY = 10

# GameOver text
gameover_font = pygame.font.Font('Lalezar-Regular.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    gameover_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


def fire_heart(x, y):
    global heart_state
    heart_state = "fire"
    screen.blit(heartImg, (x + 16, y + 10))


def is_collision(alienX, alienY, heartX, heartY):
    distance = math.sqrt((math.pow(alienX - heartX, 2)) + (math.pow(alienY - heartY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop

running = True
while running:
    # RGB
    screen.fill((136, 174, 208))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if heart_state == "ready":
                    heart_sound = mixer.Sound('laser.wav')
                    heart_sound.play()
                    heartX = playerX
                    fire_heart(heartX, heartY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries for spaceship, so it doesn't go out of bounds.
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_aliens):

        # Game Over
        if alienY[i] > 440:
            for j in range(num_of_aliens):
                alienY[j] = 2000
            game_over()
            break

        alienX[i] += alienX_change[i]

        if alienX[i] <= 0:
            alienX_change[i] = 0.5
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -0.3
            alienY[i] += alienY_change[i]

        # Collision
        collision = is_collision(alienX[i], alienY[i], heartX, heartY)
        if collision:
            collision_sound = mixer.Sound('mixkit-fairy-magic-sparkle-871.wav')
            collision_sound.play()
            heartY = 480
            heart_state = "ready"
            score_value += 1
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(50, 150)
        alien(alienX[i], alienY[i], i)
    import random
    import math
    import pygame
    import random
    from pygame import mixer

    # Initialize the pygame
    pygame.init()
    # Create a screen
    screen = pygame.display.set_mode((800, 600))

    game_state = "start_menu"

    # Background
    background = pygame.image.load('kitt.jpg')

    # Background sound
    mixer.music.load('heartlazer.mp3')
    mixer.music.play(-1)

    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('001-rocket.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Alien
    alienImg = []
    alienX = []
    alienY = []
    alienX_change = []
    alienY_change = []
    num_of_aliens = 6
    for i in range(num_of_aliens):
        alienImg.append(pygame.image.load('alien.png'))
        alienX.append(random.randint(0, 736))
        alienY.append(random.randint(50, 150))
        alienX_change.append(0.5)
        alienY_change.append(40)

    # Heart
    # Ready - You can't see the heart on the screen
    # Fire - the heart is moving
    heartImg = pygame.image.load('heart.png')
    heartX = 0
    heartY = 480
    heartX_change = 0
    heartY_change = 5
    heart_state = "ready"

    # Game start text

    start = pygame.font.Font('Lalezar-Regular.ttf', 64)

    # Score
    score_value = 0
    font = pygame.font.Font('Lalezar-Regular.ttf', 32)
    textX = 10
    textY = 10

    # GameOver text
    gameover_font = pygame.font.Font('Lalezar-Regular.ttf', 64)


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def game_over():
        gameover_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameover_text, (200, 250))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def alien(x, y, i):
        screen.blit(alienImg[i], (x, y))


    def fire_heart(x, y):
        global heart_state
        heart_state = "fire"
        screen.blit(heartImg, (x + 16, y + 10))


    def is_collision(alienX, alienY, heartX, heartY):
        distance = math.sqrt((math.pow(alienX - heartX, 2)) + (math.pow(alienY - heartY, 2)))
        if distance < 27:
            return True
        else:
            return False


    # Game Loop

    running = True
    while running:
        # RGB
        screen.fill((136, 174, 208))

        # Background image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1
                if event.key == pygame.K_SPACE:
                    if heart_state == "ready":
                        heart_sound = mixer.Sound('laser.wav')
                        heart_sound.play()
                        heartX = playerX
                        fire_heart(heartX, heartY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Checking for boundaries for spaceship, so it doesn't go out of bounds.
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_aliens):

            # Game Over
            if alienY[i] > 440:
                for j in range(num_of_aliens):
                    alienY[j] = 2000
                game_over()
                break

            alienX[i] += alienX_change[i]

            if alienX[i] <= 0:
                alienX_change[i] = 0.5
                alienY[i] += alienY_change[i]
            elif alienX[i] >= 736:
                alienX_change[i] = -0.3
                alienY[i] += alienY_change[i]

            # Collision
            collision = is_collision(alienX[i], alienY[i], heartX, heartY)
            if collision:
                collision_sound = mixer.Sound('mixkit-fairy-magic-sparkle-871.wav')
                collision_sound.play()
                heartY = 480
                heart_state = "ready"
                score_value += 1
                alienX[i] = random.randint(0, 736)
                alienY[i] = random.randint(50, 150)
            alien(alienX[i], alienY[i], i)

        # Heart movement
        if heartY <= 0:
            heartY = 480
            heart_state = "ready"
        if heart_state == "fire":
            fire_heart(heartX, heartY)
            heartY -= heartY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    # Heart movement
    if heartY <= 0:
        heartY = 480
        heart_state = "ready"
    if heart_state == "fire":
        fire_heart(heartX, heartY)
        heartY -= heartY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
