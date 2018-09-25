import pygame
import random
import time


pygame.init()
display_width = 800
display_height = 600
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
monkey_width = 80

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Monkey Dodge')
clock = pygame.time.Clock()

        
monkeyImg = pygame.image.load('MonkeyDodge.png')
background = pygame.image.load('MonkeyBackground.jpg')


def things_dodged(count):
   font = pygame.font.SysFont(None,25)
   text = font.render("Dodged: "+ str(count), True, blue)
   gameDisplay.blit(text,(0,0))

def blocks(x_loc, y_loc, w_loc, h_loc, color):
   pygame.draw.rect(gameDisplay, color, [x_loc, y_loc, w_loc, h_loc])

def monkey(x,y):
   gameDisplay.blit(monkeyImg,(x,y))

def text_objects(text, font):
   textSurface = font.render(text, True, red)
   return textSurface, textSurface.get_rect()
   

def message_display(text):
   largeText = pygame.font.Font('freesansbold.ttf', 115)
   TextSurf, TextRect = text_objects(text, largeText)
   TextRect.center = ((display_width/2),(display_height/2))
   gameDisplay.blit(TextSurf, TextRect)

   pygame.display.update()
   time.sleep(1)

   game_loop()

def crash():
   message_display('You crashed')

def game_loop():

   x = (display_width * 0.45)
   y = (display_height * 0.89)

   x_change = 0

   block_starty = -600
   block_speed = 7
   block_width = 100
   block_height = 100
   block_startx = random.randrange(0, (display_width-block_width))

   dodged = 0

   gameExit = False

   while not gameExit:
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change = -5
            elif event.key == pygame.K_RIGHT:
               x_change = 5
               

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0
            
         
      x+= x_change

      gameDisplay.fill(white)
      gameDisplay.blit(background, (0,0))
      things_dodged(dodged)
      items = blocks(block_startx, block_starty, block_width, block_height, white)

         
      
      block_starty += block_speed       
      monkey(x,y)
      
      

      if x > display_width - monkey_width or x<0:
         crash()
 
      if block_starty > display_height:
         block_starty = 0 - block_height
         block_startx = random.randrange(0,(display_width - block_width))
         dodged += 1
         block_speed += .3
         
      
      if y < block_starty + block_height:
         if x > block_startx and x < block_startx + block_width \
            or x + monkey_width > block_startx and x + monkey_width < block_startx + block_width:
            crash()
         
      
      pygame.display.update()
      clock.tick(60)

game_loop()
pygame.quit()
quit()
