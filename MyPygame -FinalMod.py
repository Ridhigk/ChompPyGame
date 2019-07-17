# Ridhi Gopalakrishnan, 718263
# The Woodlands School, ICS3U0
# This program is my PyGame. Instructions for gameplay can be found on the first screen once the program is run.

import pygame
import random



# Using the Sprite class to create a Sprite that will be controlled by the player.
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, imgname):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgname)
        self.rect = self.image.get_rect()
        self.rect.center = pos

# Using the Sprite class to create Sprites that the player will have to "eat."
class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos, imgname):
        pygame.sprite.Sprite.__init__(self)
        self.name = imgname
        self.image = pygame.image.load(imgname)
        self.rect = self.image.get_rect()
        self.rect.center = pos

# Setting up general PyGame components.
fps = 50
bg = pygame.image.load("background.jpg")
green = (0, 255, 0)
black = (0, 0, 0)
size = [800, 600]

pygame.init()
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chomp!")

# Setting up attributes of the Sprite that the player will control.
players = [Player([400, 300], "elephant.png"), Player([400, 300], "toucan.png"), Player([400, 300], "monkey.png")]
player_group = pygame.sprite.Group()

# Setting up attributes of the Sprites that the player will have to "eat."
fruits = [Fruit([50, 100], "apple.png"), Fruit([300, 500], "apple.png"),  Fruit([625, 325], "apple.png"), Fruit([200, 60], "banana.png"), Fruit([75, 475], "banana.png"), Fruit([700, 150], "banana.png"), Fruit([650, 550], "orange.png"), Fruit([150, 300], "orange.png"), Fruit([480, 50], "orange.png")]
fruit_group = pygame.sprite.Group()

# All sprites group.
all_sprites = pygame.sprite.Group()

player = [Player([400, 300], "elephant.png")]


def setup_player_fruit():
    for i in range(0,3):
        player_group.add(players[i])

    # Randomly generating animal that is the Sprite that the player will control.
    sprs = iter(player_group.sprites())

    for a in sprs:
        if random.randint(1,3) == 1:
            player = players[0]
            player.name = "elephant"

        if random.randint(1,3) == 2:
            player = players[1]
            player.name = "toucan"

        if random.randint(1,3) == 3:
            player = players[2]
            player.name = "monkey"

    # Setting up attributes of movement.           
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 3
    player.vy = 3
      
    for i in range(0,9):
        fruit_group.add(fruits[i])
   
    all_sprites.add(player)    
               
    for i in range(0,9):
        all_sprites.add(fruits[i])
    



            
    
# Main program loop:
stillPlaying = True
instructionState = True
playingState = False
gameoverState = False
restartState = False
winState = False
lossState = False

setup_player_fruit()

while stillPlaying:
    clock.tick(fps)
    
    # Step 1: Processing events - user inputs
    # Responding to quit command.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stillPlaying = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            instructionState = False
            playingState = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print ("Space pressed")
            if restartState == True:
                
                for i in range(0,9):                        
                    fruit_group.add(fruits[i])
                    all_sprites.add(fruits[i])
                 # Randomly generating animal that is the Sprite that the player will control.
                sprs = iter(player_group.sprites())

                for a in sprs:
                    if random.randint(1,3) == 1:
                        player = players[0]
                        player.name = "elephant"
                                                    
                    if random.randint(1,3) == 2:
                        player = players[1]
                        player.name = "toucan"

                    if random.randint(1,3) == 3:
                        player = players[2]
                        player.name = "monkey"

                # Setting up attributes of movement.
                player.rect.x = 400
                player.rect.y = 300
                player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
                player.vx = 3
                player.vy = 3
                                    
                all_sprites.add(player)   
                playingState = True
                restartState = False
        
    # Responding to key presses.
    key = pygame.key.get_pressed()

    if (key[player.move[0]]):
            
            player.rect.x += player.vx * (-1)
            
    if (key[player.move[1]]):
            
            player.rect.x += player.vx * (1)      

    if (key[player.move[2]]):
            
            player.rect.y += player.vy * (-1)
            
    if (key[player.move[3]]):
            
            player.rect.y += player.vy * (1)

    if playingState == True:            

        # Ensure Sprite that player controls will not go off the screen.
        if player.rect.right > 800:
            player.rect.right = 800

        if player.rect.top < - 50:
            player.rect.top = - 50

        if player.rect.bottom > 640:
            player.rect.bottom = 640

        if player.rect.left < 0:
            player.rect.left = 0

        # Removing correct fruit if player "eats" it and ending game if incorrect fruit is "eaten."
        for i in range(0,9):
            if pygame.sprite.collide_rect(player, fruits[i]) == True:
                if (player.name == "elephant" and fruits[i].name == "apple.png"):
                    pygame.sprite.Sprite.kill(fruits[i])
                                            
                elif (player.name == "toucan" and fruits[i].name == "orange.png"):
                    pygame.sprite.Sprite.kill(fruits[i])
                    
                elif (player.name == "monkey" and fruits[i].name == "banana.png"):
                    pygame.sprite.Sprite.kill(fruits[i])

                else:
                    print ("wrong collission")
                    playingState = False
                    lossState = True
                    winState = False
                    all_sprites.empty()
                    #fruit_group.empty()
                    
                    
               
        if (len(fruit_group.sprites()) == 0):
            all_sprites.empty()
            playingState = False
            winState = True

        # Step 2: Updating the game
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        # Randomly swapping out fruits every 3+ seconds.
        if seconds > 3:
            start_ticks = pygame.time.get_ticks()
            sprs = iter(fruit_group.sprites())

            for a in sprs:
                if random.randint(1,3) == 1:
                    a.image = pygame.image.load("apple.png")
                    a.name = "apple.png"

                if random.randint(1,3) == 2:
                    a.image = pygame.image.load("orange.png")
                    a.name = "orange.png"

                if random.randint(1,3) == 3:
                    a.image = pygame.image.load("banana.png")
                    a.name = "banana.png"
        
        pygame.display.update()
        

        # Step 3: Drawing / rendering on-screen
        # Redirecting to "You Win!" or "You Lose!" screen.
        #print (currentWin)
        #print("1. " + str(len(fruit_group.sprites())) + str(playingState))
     
        if (len(fruit_group.sprites()) > 0 and playingState == True):
            
            screen.blit(bg, [0,0])
            all_sprites.draw(screen)
            pygame.display.flip()
                    
        else:
            font = pygame.font.Font('freesansbold.ttf', 32)

            #print (currentWin)
                    
            if winState == True:
                print ("win")
                text = font.render("You Win! Press space to continue", True, green)
                restartState = True
                
            elif lossState == True:
                print ("Lose")
                text = font.render("You Lose! Press space to continue", True, green)
                restartState = True
                

            textRect = text.get_rect()  
            textRect.center = (400, 300)
            
            screen.fill(black)
            all_sprites.draw(screen)
            screen.blit(text, textRect)
            winState = False
            lossState = False
                 
            pygame.display.flip()

    elif instructionState == True:
            
        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render("Welcome to the game, Monkey can eat banana, Elephant can eat Apple and Toucan orange Press enter to continue", True, green)
                        
    
        textRect = text.get_rect()  
        textRect.center = (400, 300)

        screen.fill(black)
        
        screen.blit(text, textRect)
        #blit_text(screen, text, (20, 20), font)
             
        pygame.display.flip()
            
        
pygame.quit()

