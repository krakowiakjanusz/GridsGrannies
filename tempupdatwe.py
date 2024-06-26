import pygame
import math
import random

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize font module
clock = pygame.time.Clock()

#displaywindow setup
# Display window variables
width = 750
height = 750
# Display window setup
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projectile Bouncing otherball')

# Define a font for text
bigFont = pygame.font.SysFont('Georgia', 40, bold=True)  
smallFont = pygame.font.SysFont('Georgia', 24, bold=True)


# Render text surfaces
# welcome text
welcome = bigFont.render('Grids, Grannies and', True, (255, 255, 255)) 
welcome1 = bigFont.render('Gratuitous Violence', True, (255, 255, 255))
# start button
start = bigFont.render('Start', True, (255,255,255)) 
# render decision text
decideText = bigFont.render('Whose side will you take?!', True, (255,255,255))
# render "Granny" text
granny = bigFont.render('Granny', True, (255,255,255))  
 # render "Child" text
child = bigFont.render('Child', True, (255,255,255)) 

# coordinates text
coordinatesText = smallFont.render('Pick your 5 x,y coordinates for the computer to try and hit', True, (255,255,255))
xText = smallFont.render('Pick your x co-ordinate', True, (255,255,255))
yText = smallFont.render('Pick your y co-ordinate', True, (255,255,255))

# number text
Text1 = bigFont.render('1', True, (255, 255, 255)) # Render '1' text
Text2 = bigFont.render('2', True, (255, 255, 255)) # Render '2' text
Text3 = bigFont.render('3', True, (255, 255, 255)) # Render '3' text
Text4 = bigFont.render('4', True, (255, 255, 255)) # Render '4' text
Text5 = bigFont.render('5', True, (255, 255, 255)) # Render '5' text

# throwing text
throwingPosExplainer = smallFont.render('click a button to chose the X cord of what you want to hit', True, (20, 20, 20)) #instructions for the button page
ballThrowingExplainer = smallFont.render('click the mouse to throw the ball', True, (20, 20, 20)) # instruction for shooting page
ballThrowingExplainer1 = smallFont.render('the section the ball lands in is your Y cord', True, (20, 20, 20))
sucsessfullThrow = bigFont.render('WELL DONE YOUVE HIT', True, (255, 255, 255)) # sucsessfull shot text
sucsessfullThrow1 = smallFont.render('click to continue', True, (255, 255, 255)) # click to continue tdxt for shooting page
unsucsessfullThrow = bigFont.render('YOUVE MISSED', True, (255, 255, 255)) # unsucsessfull shot text
friendlyWin = bigFont.render('PLAYER WIN', True, (255, 255, 255)) # other turn text
enemyWin = bigFont.render('ENEMY WIN', True, (255, 255, 255)) # other turn text
enemyHit = bigFont.render('ENEMY HIT', True, (255, 255, 255)) # ither hit text
enemyMiss = bigFont.render('ENEMY MISS', True, (255, 255, 255)) # enemym ises text

# Define button rectangles for interaction
button = pygame.Rect(width // 2 - 55,215,110,60)  # Start button
grannyButton = pygame.Rect(500,300,170,60)  # Granny selection button
kidButton = pygame.Rect(500, 400, 170, 60)  # Child selection button
xButton1 = pygame.Rect(10, 150, 138, 60) # x box 1
xButton2 = pygame.Rect(158, 150, 138, 60) # x box 2
xButton3 = pygame.Rect(306, 150, 138, 60) # x box 3
xButton4 = pygame.Rect(454, 150, 138, 60) # x box 4
xButton5 = pygame.Rect(602, 150, 138, 60) # x box 5
yButton1 = pygame.Rect(10, 300, 138, 60) # y box 1
yButton2 = pygame.Rect(158, 300, 138, 60) # y box 2
yButton3 = pygame.Rect(306, 300, 138, 60) # y box 3
yButton4 = pygame.Rect(454, 300, 138, 60) # y box 4
yButton5 = pygame.Rect(602, 300, 138, 60) # y box 5
throwingPosButton1 = pygame.Rect(10, 650, 138, 60) #throwing position 1 box
throwingPosButton2 = pygame.Rect(158, 650, 138, 60) #throwing position 2 box
throwingPosButton3 = pygame.Rect(306, 650, 138, 60) #throwing position 3 box
throwingPosButton4 = pygame.Rect(454, 650, 138, 60) #throwing position 4 box
throwingPosButton5 = pygame.Rect(602, 650, 138, 60) #throwing position 5 box

#loading the background image
ballThrowing = pygame.image.load("projectile_background.jpg").convert_alpha()
ballThrowing = pygame.transform.scale(ballThrowing, (750, 750))
# Load and scale background images for different screens
menu = pygame.image.load("menuScreen.jpg").convert_alpha()  # Load menu screen background
menu = pygame.transform.scale(menu, (750, 750))  # Scale to fit window
enemyresult = pygame.image.load("enemy_result.jpg").convert_alpha()  # Load menu screen background
enemyresult = pygame.transform.scale(enemyresult, (750, 750))  # Scale to fit window
decide = pygame.image.load("decideScreen.jpg").convert_alpha()  # Load decision screen background
decide = pygame.transform.scale(decide, (750, 750))  # Scale to fit window
throwingPos = pygame.image.load("menuScreen.jpg").convert_alpha()  # Load action screen background
throwingPos = pygame.transform.scale(throwingPos, (750, 750))  # Scale to fit window
coordinatesScreen = pygame.image.load("menuScreen.jpg").convert_alpha()
coordinatesScreen = pygame.transform.scale(coordinatesScreen, (750, 750))

selectedSide=""  # variable to store the selected side
# stores the player shots 
playerXCord = 0 
playerYCord = 0
# stores the location of the target object 
objectXCord = 2
objectYCord = 2
# stores players chosen coordinates
playerX1 = 0
playerX2 = 0
playerX3 = 0
playerX4 = 0
playerX5 = 0
playerY1 = 0
playerY2 = 0
playerY3 = 0
playerY4 = 0
playerY5 = 0
# determines what coordinate is being selected
xCounter = 0
yCounter = 0

#Counts how many enemies have been hit
playerHitCount = 0

#counts how many players have been hit
enemyHitCount = 0

#Boolean to determine if the computer has hit an object this turn.
computerhitornot = False

#Boolean to determine if the computer has won.
computerWin = False

#Boolean to determine if the computer has won.
PlayerWin = False

        
        
        
        
        
        
        
# Randomise computer objects 1 and 2.
computerX1 = random.randint(1, 5)
computerY1 = random.randint(1, 5)

computerX2 = random.randint(1, 5)
computerY2 = random.randint(1, 5)

# Error check for objects being equal to each other.
while computerX1 == computerX2 and computerY1 == computerY2:
    computerY2 = random.randint(1, 5)

# Randomise computer object 3.
computerX3 = random.randint(1, 5)
computerY3 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX3 == computerX1:
    while computerY3 == computerY1:
        computerY3 = random.randint(1, 5)
if computerX3 == computerX2:
   while computerY3 == computerY2:
        computerY3 = random.randint(1, 5)
    
# Randomise computer object 4.
computerX4 = random.randint(1, 5)
computerY4 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX4 == computerX1:
    while computerY4 == computerY1:
        computerY4 = random.randint(1, 5)
if computerX4 == computerX2:
    while computerY4 == computerY2:
        computerY4 = random.randint(1, 5)
if computerX4 == computerX3:
    while computerY4== computerY3:
        computerY4 = random.randint(1, 5)

# Randomise computer object 5.
computerX5 = random.randint(1, 5)
computerY5 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX5 == computerX1:
    while computerY5 == computerY1:
        computerY5 = random.randint(1, 5)
if computerX5 == computerX2:
    while computerY5 == computerY2:
        computerY5 = random.randint(1, 5)
if computerX5== computerX3:
    while computerY5== computerY3:
        computerY5 = random.randint(1, 5)
if computerX5 == computerX4:
    while computerY5 == computerY4:
        computerY5 = random.randint(1, 5)
 
print (computerX1)
print (computerX2)
print (computerX3)
print (computerX4)
print (computerX5)
print (computerY1)
print (computerY2)
print (computerY3)
print (computerY4)
print (computerY5)        
# wall properties
wall_width = 20  # width of the wall
wall_height = height // 2 + 30  # 1/3 of the screen height
wall_x = 245 - wall_width // 2  # center the wall on the screen
wall_y = height - wall_height  # position the wall vertically in the middle

# calculate the width of the score segments to the right of the wall
segment_width = (width - (wall_x + wall_width)) / 5

message_displayed = False  # global variable to track message display state
landing_segment = 0  # track which segment the ball lands in

class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velx = 0  # Horizontal velocity
        self.vely = 0  # Vertical velocity
        self.shoot = False

    def draw(self, window):
        # draw weapon
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        global message_displayed, landing_segment
        if self.shoot:
            self.x += self.velx
            self.y += self.vely
            self.vely += 0.1  # Gravity effect

            # Bounce off the left or right screen edge
            if self.x <= self.radius or self.x >= width - self.radius:
                self.velx *= -1

            # Bounce off the top screen edge
            if self.y <= self.radius:
                self.vely *= -1

            # Stick to the bottom screen edge and stop
            if self.y >= height - self.radius - 30:
                self.velx = 0
                self.vely = 0
                self.y = height - self.radius - 30
                self.shoot = False

            # Wall collision detection for the x axis
            if wall_y <= self.y <= wall_y + wall_height:
                # Check if the ball hits the side of the wall
                if wall_x <= self.x <= wall_x + wall_width:
                    self.velx *= -1 # Reverse the horizontal velocity
            
            # Detect landing on the right side of the wall
            if self.x > wall_x + wall_width and self.y >= height - self.radius -30:
                message_displayed = True
                self.shoot = False
                # Calculate the segment number (1 to 5) where the ball landed
                landing_segment = int((self.x - (wall_x + wall_width)) / segment_width) + 1
                landing_segment = min(landing_segment, 5)  # Ensure it doesn't exceed 5
                #playerYCord = landing_segment
    
    
    def shootProjectile(self, pos):
        if not self.shoot:
            self.shoot = True
            angle = math.atan2(pos[1] - self.y, pos[0] - self.x)
            power = min(math.sqrt((pos[1] - self.y)**2 + (pos[0] - self.x)**2) / 35, 10)
            self.velx = math.cos(angle) * power
            self.vely = math.sin(angle) * power

# Initialize projectile
weapon = Projectile(50, 600, 12, (223, 255, 79))

# Main game loop
bg = menu
run = True
while run:
    window.blit(bg,bg.get_rect()) #draw the background
    a, b = pygame.mouse.get_pos()  # Get current mouse position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button press
            
            if bg == menu:
                if button.collidepoint(event.pos):  # If "Start" button is pressed
                    bg = decide  # Change background to decision screen
            
            elif bg == decide:
                if grannyButton.collidepoint(event.pos):  # If "Granny" button is pressed
                    bg = coordinatesScreen  # Change background to action screen
                    selectedSide = "Granny"  # Set selected side to Granny
                    print(selectedSide)
                elif kidButton.collidepoint(event.pos):  # If "Child" button is pressed
                    bg = coordinatesScreen  # Change background to action screen
                    selectedSide = "Child"  # Set selected side to Child
                    print(selectedSide)

            elif bg == coordinatesScreen:
                # registers button collisions for players selected coordinates- only stores the first 5 x,y pressed
                # not fully validated ie. can pick 3 x coords then 2 y etc.
                # you can also technically pick the same x and y 5 times
                if xButton1.collidepoint(event.pos):
                    xCounter += 1
                    if xCounter == 1:
                        playerX1 = 1
                    elif xCounter == 2:
                        playerX2 = 1
                    elif xCounter == 3:
                        playerX3 = 1
                    elif xCounter == 4:
                        playerX4 = 1
                    elif xCounter == 5:
                        playerX5 = 1

                if xButton2.collidepoint(event.pos):
                    xCounter += 1
                    if xCounter == 1:
                        playerX1 = 2
                    elif xCounter == 2:
                        playerX2 = 2
                    elif xCounter == 3:
                        playerX3 = 2
                    elif xCounter == 4:
                        playerX4 = 2
                    elif xCounter == 5:
                        playerX5 = 2

                if xButton3.collidepoint(event.pos):
                    xCounter += 1
                    if xCounter == 1:
                        playerX1 = 3
                    elif xCounter == 2:
                        playerX2 = 3
                    elif xCounter == 3:
                        playerX3 = 3
                    elif xCounter == 4:
                        playerX4 = 3
                    elif xCounter == 5:
                        playerX5 = 3

                if xButton4.collidepoint(event.pos):
                    xCounter += 1
                    if xCounter == 1:
                        playerX1 = 4
                    elif xCounter == 2:
                        playerX2 = 4
                    elif xCounter == 3:
                        playerX3 = 4
                    elif xCounter == 4:
                        playerX4 = 4
                    elif xCounter == 5:
                        playerX5 = 4

                if xButton5.collidepoint(event.pos):
                    xCounter += 1
                    if xCounter == 1:
                        playerX1 = 5
                    elif xCounter == 2:
                        playerX2 = 5
                    elif xCounter == 3:
                        playerX3 = 5
                    elif xCounter == 4:
                        playerX4 = 5
                    elif xCounter == 5:
                        playerX5 = 5

                if yButton1.collidepoint(event.pos):
                    yCounter += 1
                    if yCounter == 1:
                        playerY1 = 1
                    elif yCounter == 2:
                        playerY2 = 1
                    elif yCounter == 3:
                        playerY3 = 1
                    elif yCounter == 4:
                        playerY4 = 1
                    elif yCounter == 5:
                        playerY5 = 1

                if yButton2.collidepoint(event.pos):
                    yCounter += 1
                    if yCounter == 1:
                        playerY1 = 2
                    elif yCounter == 2:
                        playerY2 = 2
                    elif yCounter == 3:
                        playerY3 = 2
                    elif yCounter == 4:
                        playerY4 = 2
                    elif yCounter == 5:
                        playerY5 = 2

                if yButton3.collidepoint(event.pos):
                    yCounter += 1
                    if yCounter == 1:
                        playerY1 = 3
                    elif yCounter == 2:
                        playerY2 = 3
                    elif yCounter == 3:
                        playerY3 = 3
                    elif yCounter == 4:
                        playerY4 = 3
                    elif yCounter == 5:
                        playerY5 = 3

                if yButton4.collidepoint(event.pos):
                    yCounter += 1
                    if yCounter == 1:
                        playerY1 = 4
                    elif yCounter == 2:
                        playerY2 = 4
                    elif yCounter == 3:
                        playerY3 = 4
                    elif yCounter == 4:
                        playerY4 = 4
                    elif yCounter == 5:
                        playerY5 = 4

                if yButton5.collidepoint(event.pos):
                    yCounter += 1
                    if yCounter == 1:
                        playerY1 = 5
                    elif yCounter == 2:
                        playerY2 = 5
                    elif yCounter == 3:
                        playerY3 = 5
                    elif yCounter == 4:
                        playerY4 = 5
                    elif yCounter == 5:
                        playerY5 = 5

                if(yCounter==5) and (xCounter==5):
                    bg=throwingPos

            elif bg == throwingPos:
                if throwingPosButton1.collidepoint(event.pos):  # If throwingPosButton1 button is pressed
                    playerXCord = 1
                    print('shot x cord = 1')
                    bg = ballThrowing  # Change background to decision screen
                                 
                elif throwingPosButton2.collidepoint(event.pos):  # If throwingPosButton2 button is pressed
                    playerXCord = 2
                    print('shot x cord = 2')
                    bg = ballThrowing  # Change background to decision screen   
                
                elif throwingPosButton3.collidepoint(event.pos):  # If throwingPosButton3 button is pressed
                    playerXCord = 3
                    print('shot x cord = 3')
                    bg = ballThrowing  # Change background to decision screen
                
                elif throwingPosButton4.collidepoint(event.pos):  # If throwingPosButton4 button is pressed
                    playerXCord = 4
                    print('shot x cord = 4')
                    bg = ballThrowing  # Change background to decision screen
                     
                elif throwingPosButton5.collidepoint(event.pos):  # If throwingPosButton5 button is pressed
                    playerXCord = 5
                    print('shot x cord = 5')
                    bg = ballThrowing  # Change background to decision screen      
            
            elif bg == ballThrowing:
                HitThisTurn = False  # Reset flag to false for if player hits a piece this turn
                if message_displayed:
                    playerYCord = landing_segment
                    weapon.x = 50  # Optionally reset the projectile's position
                    weapon.y = 600
                    print('shot y cord = ' + str(landing_segment))
                    print(playerXCord, 'playerYCord = ', landing_segment)
                    
                    if playerXCord == computerX1 and computerY1 == landing_segment: # checks if player hit both part of enemy co-ords
                        playerHitCount += 1 #increments number of things player has hit
                        computerX1 =0 #sets enemy co-ords to 0 so the same piece cant be hit twice
                        computerY1 =0
                        if playerHitCount == 5: #lets player win if all 5 pieces have been hit
                            PlayerWin = True
                            
                        else:
                            print('hit!')
                            HitThisTurn = True
                            bg = throwingPos
                            message_displayed = False        
                            
                    if playerXCord == computerX2 and computerY2 == landing_segment:
                        playerHitCount += 1
                        computerX2 =0
                        computerY2 =0
                        if playerHitCount == 5:
                            PlayerWin = True
                            
                        else:
                            print('hit!')
                            HitThisTurn = True
                            bg = throwingPos
                            message_displayed = False    
                            
                    if playerXCord == computerX3 and computerY3 == landing_segment:
                        playerHitCount += 1
                        computerX3 = 0
                        computerY3 = 0
                        if playerHitCount == 5:
                            PlayerWin = True
                            
                        else:
                            print('hit!')
                            HitThisTurn = True
                            message_displayed = False
                            bg = throwingPos
                                
                    
                    if playerXCord == computerX4 and computerY4 == landing_segment:
                        playerHitCount += 1
                        computerX4 = 0
                        computerY4 = 0
                        if playerHitCount == 5:
                            PlayerWin = True
                            
                        else:
                            print('hit!')
                            HitThisTurn = True
                            message_displayed = False     
                            bg = throwingPos
                                      
                    
                    if playerXCord == computerX5 and computerY5 == landing_segment:
                        playerHitCount += 1
                        computerX5 = 0
                        computerY5 = 0
                        if playerHitCount == 5:
                            PlayerWin = True
                            
                        else:
                            print('hit!')
                            HitThisTurn = True
                            message_displayed = False  
                            bg = throwingPos
                              
                                
                    else:
                        print('miss!')
                         # Reset message display state and allow for a new shot without moving the projectile
                    message_displayed = False
                    bg = enemyresult
                    
                else:
                    pos = pygame.mouse.get_pos()
                    weapon.shootProjectile(pos)
                    
            elif bg == enemyresult:
               
                computerXGuess = random.randint(1,5)
                computerYGuess = random.randint(1,5)
                print(computerXGuess, computerYGuess)
                
                if [computerXGuess,computerYGuess] == [playerX1,playerY1]:
                    enemyHitCount += 1
                    playerX1 = 0
                    playerY1 = 0
                    if enemyHitCount == 5:
                        computerWin = True
                        print ("enemy wins!")
                                
                    else:
                        computerhitornot = True
                        print ("enemy hit!")
                        bg = throwingPos
                
                elif [computerXGuess,computerYGuess] == [playerX2,playerY2]:
                    enemyHitCount += 1
                    playerX2 = 0
                    playerY2 = 0
                    if enemyHitCount == 5:
                        computerWin = True
                        print ("enemy wins!")
                                
                    else:
                        computerhitornot = True
                        print ("enemy hit!")
                        bg = throwingPos
                
                elif [computerXGuess,computerYGuess] == [playerX3,playerY3]:
                    enemyHitCount += 1
                    playerX3 = 0
                    playerY3 = 0
                    if enemyHitCount == 5:
                        computerWin = True
                        print ("enemy wins!")
                                
                    else:
                        computerhitornot = True
                        print ("enemy hit!")
                        bg = throwingPos
                
                elif [computerXGuess,computerYGuess] == [playerX4,playerY4]:
                    enemyHitCount += 1
                    playerX4 = 0
                    playerY4 = 0
                    if enemyHitCount == 5:
                        computerWin = True
                        print ("enemy wins!")
                                
                    else:
                        computerhitornot = True
                        print ("enemy hit!")
                        bg = throwingPos
                
                elif [computerXGuess,computerYGuess] == [playerX5,playerY5]:
                    enemyHitCount += 1
                    playerX5 = 0
                    playerY5 = 0
                    if enemyHitCount == 5:
                        computerWin = True
                        print ("enemy wins!")
                                
                    else:
                        computerhitornot = True
                        print ("enemy hit!")
                        bg = throwingPos
                else:
                    computerhitornot = False
                    print ("enemy miss!")
                    bg = throwingPos        
                #if computerXGuess == playerX1:
                #        if computerYGuess == playerY1:
                #            enemyHitCount += 1
                #            playerX1 = 0
                #            playerY1 = 0
                #            if enemyHitCount == 5:
                #                computerWin = True
                #                print ("enemy wins!")
                #                
                #            else:
                #                computerhitornot = True
                #                print ("enemy hit!")
                #                bg = throwingPos
                #        else:
                #            computerhitornot = False
                #            print ("enemy miss!")
                #            bg = throwingPos
                              
                #elif computerXGuess == playerX2:
                #        if computerYGuess == playerY2:
                #            enemyHitCount += 1
                #            playerX2 = 0
                #            playerY2 = 0
                #            if enemyHitCount == 5:
                #                computerWin = True
                #                print ("enemy wins!")
                #                
                #            else:
                #                computerhitornot = True
                #                print ("enemy hit!")
                #                bg = throwingPos
                #        else:
                #            computerhitornot = False
                #            print ("enemy miss!")
                #            bg = throwingPos
                #            
                #elif computerXGuess == playerX3:
                #        if computerYGuess == playerY3:
                #            enemyHitCount += 1
                #            playerX3 = 0
                #            playerY3 = 0
                #            if enemyHitCount == 5:
                #                computerWin = True
                #                print ("enemy wins!")
                #                
                #            else:
                #                computerhitornot = True
                #                print ("enemy hit!")
                #                bg = throwingPos
                #        else:
                #            computerhitornot = False
                #            print ("enemy miss!")
                #            bg = throwingPos
                #            
                #elif computerXGuess == playerX4:
                #        if computerYGuess == playerY4:
                #            enemyHitCount += 1
                #            playerX4 = 0
                #            playerY4 = 0
                #            if enemyHitCount == 5:
                #           computerWin = True
                #                ("enemy wins!")
                #            else:
                #                computerhitornot = True
                #                print ("enemy hit!")
                #                bg = throwingPos
                #        else:
                #            computerhitornot = False
                #            print ("enemy miss!")
                #            bg = throwingPos
                            
                #elif computerXGuess == playerX5:
                #        if computerYGuess == playerY5:
                #            enemyHitCount += 1
                #            playerX5 = 0
                #            playerY5 = 0
                #            if enemyHitCount == 5:
                #                computerWin = True
                #                ("enemy wins!")
                #            else:
                #                computerhitornot = True
                #                print ("enemy hit!")
                #                bg = throwingPos
                #        else:
                #            computerhitornot = False
                #            print ("enemy miss!")
                #            bg = throwingPos                                                                                      
                #else:
                #     computerhitornot = False
                #     print ("enemy miss!")
                #     bg = throwingPos 
                     
                           
    # Button hover effects and display logic for menu screen
    if bg == menu:
        window.blit(welcome, (width // 2 - welcome.get_width() // 2, 60))
        window.blit(welcome1, (width // 2 - welcome1.get_width() // 2, 70 + welcome1.get_height()))
        if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
            pygame.draw.rect(window, (180,180,180), button)  # Highlight button on hover
        else:
            pygame.draw.rect(window, (110,110,110), button)  # Default button appearance
        window.blit(start,(button.x + 5, button.y + 5))  # Draw "Start" text on button
    
    # Button hover effects and display logic for decision screen
    elif bg == decide:
        window.blit(decideText, (width // 2 - decideText.get_width() // 2, height // 6 - decideText.get_height() // 2))
        # Granny button
        if grannyButton.x <= a <= grannyButton.x + 170 and grannyButton.y <= b <= grannyButton.y + 60:
            pygame.draw.rect(window, (180,180,180), grannyButton)  # Highlight Granny button on hover
        else:
            pygame.draw.rect(window, (110,110,110), grannyButton)  # Default Granny button appearance
        window.blit(granny,(grannyButton.x + 5, grannyButton.y + 5))  # Draw "Granny" text on button
        # Child button
        if kidButton.x <= a <= kidButton.x + 170 and kidButton.y <= b <= kidButton.y + 60:
            pygame.draw.rect(window, (180,180,180), kidButton)  # Highlight Child button on hover
        else:
            pygame.draw.rect(window, (110,110,110), kidButton)  # Default Child button appearance
        window.blit(child,(kidButton.x + 5, kidButton.y + 5))  # Draw "Child" text on button
    
    elif bg == coordinatesScreen:
        # blits coordinates explanation text
        window.blit(coordinatesText, (width // 2 - coordinatesText.get_width() // 2, 60))
        window.blit(xText, (width // 2 - xText.get_width() // 2, 100))
        window.blit(yText, (width // 2 - yText.get_width() // 2, 250))

        if xButton1.x <= a <= xButton1.x + 138 and xButton1.y <= b <= xButton1.y + 60:
            pygame.draw.rect(window, (180,180,180), xButton1)  # Highlight xButton1 on hover
        else:
            pygame.draw.rect(window, (110,110,110), xButton1)  # Default =xButton1 button appearance
        window.blit(Text1,(xButton1.x + 5, xButton1.y + 5))  # Draw '1' text on button

        if xButton2.x <= a <= xButton2.x + 138 and xButton2.y <= b <= xButton2.y + 60:
            pygame.draw.rect(window, (180,180,180), xButton2)  # Highlight xButton2 on hover
        else:
            pygame.draw.rect(window, (110,110,110), xButton2)  # Default =xButton2 button appearance
        window.blit(Text2,(xButton2.x + 5, xButton2.y + 5))  # Draw '2' text on button

        if xButton3.x <= a <= xButton3.x + 138 and xButton3.y <= b <= xButton3.y + 60:
            pygame.draw.rect(window, (180,180,180), xButton3)  # Highlight xButton3 on hover
        else:
            pygame.draw.rect(window, (110,110,110), xButton3)  # Default =xButton3 button appearance
        window.blit(Text3,(xButton3.x + 5, xButton3.y + 5))  # Draw '3' text on button

        if xButton4.x <= a <= xButton4.x + 138 and xButton4.y <= b <= xButton4.y + 60:
            pygame.draw.rect(window, (180,180,180), xButton4)  # Highlight xButton4 on hover
        else:
            pygame.draw.rect(window, (110,110,110), xButton4)  # Default =xButton4 button appearance
        window.blit(Text4,(xButton4.x + 5, xButton4.y + 5))  # Draw '4' text on button

        if xButton5.x <= a <= xButton5.x + 138 and xButton5.y <= b <= xButton5.y + 60:
            pygame.draw.rect(window, (180,180,180), xButton5)  # Highlight xButton5 on hover
        else:
            pygame.draw.rect(window, (110,110,110), xButton5)  # Default =xButton5 button appearance
        window.blit(Text5,(xButton5.x + 5, xButton5.y + 5))  # Draw '5' text on button

        if xButton1.x <= a <= yButton1.x + 138 and yButton1.y <= b <= yButton1.y + 60:
            pygame.draw.rect(window, (180,180,180), yButton1)  # Highlight xButton1 on hover
        else:
            pygame.draw.rect(window, (110,110,110), yButton1)  # Default =xButton1 button appearance
        window.blit(Text1,(yButton1.x + 5, yButton1.y + 5))  # Draw '1' text on button

        if xButton2.x <= a <= yButton2.x + 138 and yButton2.y <= b <= yButton2.y + 60:
            pygame.draw.rect(window, (180,180,180), yButton2)  # Highlight xButton2 on hover
        else:
            pygame.draw.rect(window, (110,110,110), yButton2)  # Default =xButton2 button appearance
        window.blit(Text2,(yButton2.x + 5, yButton2.y + 5))  # Draw '2' text on button

        if xButton3.x <= a <= yButton3.x + 138 and yButton3.y <= b <= yButton3.y + 60:
            pygame.draw.rect(window, (180,180,180), yButton3)  # Highlight xButton3 on hover
        else:
            pygame.draw.rect(window, (110,110,110), yButton3)  # Default =xButton3 button appearance
        window.blit(Text3,(yButton3.x + 5, yButton3.y + 5))  # Draw '3' text on button

        if xButton4.x <= a <= yButton4.x + 138 and yButton4.y <= b <= yButton4.y + 60:
            pygame.draw.rect(window, (180,180,180), yButton4)  # Highlight xButton4 on hover
        else:
            pygame.draw.rect(window, (110,110,110), yButton4)  # Default =xButton4 button appearance
        window.blit(Text4,(yButton4.x + 5, yButton4.y + 5))  # Draw '4' text on button

        if yButton5.x <= a <= yButton5.x + 138 and yButton5.y <= b <= yButton5.y + 60:
            pygame.draw.rect(window, (180,180,180), yButton5)  # Highlight xButton5 on hover
        else:
            pygame.draw.rect(window, (110,110,110), yButton5)  # Default =xButton5 button appearance
        window.blit(Text5,(yButton5.x + 5, yButton5.y + 5))  # Draw '5' text on button


    # Button hover effects and display logic for throwingPos screen
    elif bg == throwingPos:
        window.blit(throwingPosExplainer, (width // 2 - throwingPosExplainer.get_width() // 2, 60))
        if throwingPosButton1.x <= a <= throwingPosButton1.x + 138 and throwingPosButton1.y <= b <= throwingPosButton1.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton1)  # Highlight throwingPosButton1 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton1)  # Default =throwingPosButton1 button appearance
        window.blit(Text1,(throwingPosButton1.x + 5, throwingPosButton1.y + 5))  # Draw '1' text on button

        if throwingPosButton2.x <= a <= throwingPosButton2.x + 138 and throwingPosButton2.y <= b <= throwingPosButton2.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton2)  # Highlight throwingPosButton2 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton2)  # Default =throwingPosButton2 button appearance
        window.blit(Text2,(throwingPosButton2.x + 5, throwingPosButton2.y + 5))  # Draw '2' text on button

        if throwingPosButton3.x <= a <= throwingPosButton3.x + 138 and throwingPosButton3.y <= b <= throwingPosButton3.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton3)  # Highlight throwingPosButton3 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton3)  # Default =throwingPosButton3 button appearance
        window.blit(Text3,(throwingPosButton3.x + 5, throwingPosButton3.y + 5))  # Draw '3' text on button

        if throwingPosButton4.x <= a <= throwingPosButton4.x + 138 and throwingPosButton4.y <= b <= throwingPosButton4.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton4)  # Highlight throwingPosButton4 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton4)  # Default =throwingPosButton4 button appearance
        window.blit(Text4,(throwingPosButton4.x + 5, throwingPosButton3.y + 5))  # Draw '4' text on button

        if throwingPosButton5.x <= a <= throwingPosButton5.x + 138 and throwingPosButton5.y <= b <= throwingPosButton5.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton5)  # Highlight throwingPosButton5 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton5)  # Default =throwingPosButton5 button appearance
        window.blit(Text5,(throwingPosButton5.x + 5, throwingPosButton5.y + 5))  # Draw '5' text on button

    # display logic for ballThrowing screen
    elif bg == ballThrowing:
        window.blit(ballThrowingExplainer, (width // 2 - ballThrowingExplainer.get_width() // 2, 60))
        window.blit(ballThrowingExplainer1, (width // 2 - ballThrowingExplainer1.get_width() // 2, 70 + ballThrowingExplainer1.get_height()))
        weapon.draw(window)
        pygame.draw.rect(window, (255, 255, 255), (wall_x, wall_y, wall_width, wall_height))
        if message_displayed:
            if playerXCord == objectXCord and objectYCord == landing_segment:
                window.blit(sucsessfullThrow, (width // 2 - sucsessfullThrow.get_width() // 2, height // 3 - sucsessfullThrow.get_height() //2 ))
                window.blit(sucsessfullThrow1, (width // 2 - sucsessfullThrow1.get_width() // 2, height// 3 + sucsessfullThrow1.get_height()))
            else:
                window.blit(unsucsessfullThrow, (width //2 - unsucsessfullThrow.get_width() // 2, height // 3 - unsucsessfullThrow.get_height() // 2))
                
    elif bg == enemyresult:
        if message_displayed == False:
            if computerWin == True:
                window.blit(enemyWin, (width // 2 - enemyWin.get_width() // 2, height // 3 - enemyWin.get_height() //2 ))
                window.blit(enemyWin, (width // 2 - enemyWin.get_width() // 2, height// 3 + enemyWin.get_height()))
            elif computerhitornot == True:
                window.blit(enemyHit, (width // 2 - enemyHit.get_width() // 2, height // 3 - enemyHit.get_height() //2 ))
                window.blit(enemyHit, (width // 2 - enemyHit.get_width() // 2, height// 3 + enemyHit.get_height()))
            elif computerhitornot == False:
                window.blit(enemyMiss, (width //2 - enemyMiss.get_width() // 2, height // 3 - enemyMiss.get_height() // 2))            
        
        


    weapon.update()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
