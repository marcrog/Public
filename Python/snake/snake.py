import pygame as pg
import random
import sys
from pygame.math import Vector2



def disegna(x,y):
    temp = pg.Rect(x, y, w, w)
    pg.draw.rect(screen, snake_color, temp)


def stampa_lista(lista):
    for pezzo in lista:
        disegna(pezzo.x, pezzo.y)


def move_snake(lista, s_x, s_y):
    i = 0
    for pezzo in lista:
        if i == 0:
            prec_x = pezzo.x
            prec_y = pezzo.y
        
            pezzo.x += s_x
            pezzo.y += s_y
            i = 1
        else:
            temp_x = pezzo.x
            temp_y = pezzo.y

            pezzo.x = prec_x
            pezzo.y = prec_y

            prec_x = temp_x
            prec_y = temp_y
    

    temp = Vector2(prec_x, prec_y)
    return temp


def check_lista(pos, list):
    a = 0
    for pezzo in list:
        if a == 0:
            a = 1
        elif (pezzo == pos):
            return False
    return True


def check(pos):
    if (pos.x + w <= 0 or pos.x >= screen_width or pos.y + w <= 0 or pos.y >= screen_height):
        return False 
    if check_lista(pos, list) == False:
        return False
        
#Inizializzazione------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pg.init()
clock = pg.time.Clock()

#Screen_Setup
screen_width = 600
screen_height = 600
# w = screen_width / 20
w = screen_width / 20
spost = w
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Snake')

#Colors and Snake details
snake_color = pg.Color('green')
food_color = pg.Color('red')
s_width = 30


##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Snake Inizialization

piece = Vector2(screen_width/2, screen_height/2)

speed = Vector2(0, 0)

list = [
        piece
        ]
j = 0
contact = False



#GAME LOOP ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
      

        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_UP:
                speed.x = 0
                speed.y = -spost
            if event.key == pg.K_DOWN:
                speed.x = 0
                speed.y = spost
    
            if event.key == pg.K_RIGHT:
                speed.x = spost
                speed.y = 0

            if event.key == pg.K_LEFT:
                speed.x = -spost
                speed.y = 0

    
    
    screen.fill(pg.Color('Black'));

    if j == 0 or contact:
        f_x = random.randrange(0,screen_width,w)  
        f_y = random.randrange(0,screen_width,w)
        j = 1
        contact = False
    Cibo = pg.Rect(f_x, f_y, w, w)
    pg.draw.rect(screen, food_color, Cibo)



    precedente = move_snake(list, speed.x, speed.y)

    if check(list[0]) == False:
        pg.quit()
        sys.exit()

    stampa_lista(list)

    if list[0].x == f_x and list[0].y == f_y:
        list.append(precedente)
        print(len(list))
        contact = True
    
    #Screen Update Controll
    
    a = 5
    frame = a + len(list) / 3
    if(frame > 8):
        frame = 8.5
    pg.display.flip()
    clock.tick(frame)
    

            

