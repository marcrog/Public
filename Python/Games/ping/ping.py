import pygame, sys

#Functions
def ball_animations():
    global ball_speed_x
    global ball_speed_y

    ball.x += ball_speed_x 
    ball.y += ball_speed_y

    if ball.right >= screen_width or ball.left <= 0:
       ball_speed_x *= -1
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#General Seup
pygame.init()
clock = pygame.time.Clock()

#Setup Display
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


#Colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#Game Objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
opponent = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
player = pygame.Rect(10, screen_height/2 - 70, 10, 140)


ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 0
increase_speed = 10

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#--/

            
    ball_animations()
    player.y += player_speed
    opponent.y += opponent_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


    #Visulas
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))


    pygame.display.flip()
    clock.tick(100)
