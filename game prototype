import pygame
import math

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
pygame.display.set_caption("Projectile Bouncing otherball")

# Define a font for text
bigFont = pygame.font.SysFont('Georgia', 40, bold=True)  
smallFont = pygame.font.SysFont('Georgia', 24, bold=True)


# Render text surfaces
welcome = bigFont.render('Grids, Grannies and', True, (0, 0, 0)) # render 'the welcome text
welcome1 = bigFont.render('Gratuitous Violence', True, (0, 0, 0))
start = bigFont.render('Start', True, (255,255,255))  # Render "Start" text
decideText = bigFont.render('Whose side will you take?!', True, (255,255,255))  # Render decision text
granny = bigFont.render('Granny', True, (255,255,255))  # Render "Granny" text
child = bigFont.render('Child', True, (255,255,255))  # Render "Child" text
throwingPosText1 = bigFont.render('1', True, (255, 255, 255)) # Render '1' text
throwingPosText2 = bigFont.render('2', True, (255, 255, 255)) # Render '2' text
throwingPosText3 = bigFont.render('3', True, (255, 255, 255)) # Render '3' text
throwingPosText4 = bigFont.render('4', True, (255, 255, 255)) # Render '4' text
throwingPosText5 = bigFont.render('5', True, (255, 255, 255)) # Render '5' text
throwingPosExplainer = smallFont.render('click a button to chose your X cord', True, (20, 20, 20)) #instructions for the button page
ballThrowingExplainer = smallFont.render('click the mouse to throw the ball', True, (20, 20, 20)) # instruction for shooting page
ballThrowingExplainer1 = smallFont.render('the section the ball lands in is your Y cord', True, (20, 20, 20))
sucsessfullThrow = bigFont.render('WELL DONE YOUVE HIT', True, (255, 255, 255)) # sucsessfull shot text
sucsessfullThrow1 = smallFont.render('click to continue', True, (255, 255, 255)) # click to continue tdxt for shooting page
unsucsessfullThrow = bigFont.render('YOUVE MISSED', True, (255, 255, 255)) # unsucsessfull shot text

# Define button rectangles for interaction
button = pygame.Rect(width // 2 - 55,215,110,60)  # Start button
grannyButton = pygame.Rect(500,300,170,60)  # Granny selection button
kidButton = pygame.Rect(500, 400, 170, 60)  # Child selection button
throwingPosButton1 = pygame.Rect(10, 650, 138, 60) #throwing position 1 box
throwingPosButton2 = pygame.Rect(158, 650, 138, 60) #throwing position 2 box
throwingPosButton3 = pygame.Rect(306, 650, 138, 60) #throwing position 3 box
throwingPosButton4 = pygame.Rect(454, 650, 138, 60) #throwing position 4 box
throwingPosButton5 = pygame.Rect(602, 650, 138, 60) #throwing position 5 box

#loading the backgroung image
ballThrowing = pygame.image.load('projectile_background.jpg').convert_alpha()
ballThrowing = pygame.transform.scale(ballThrowing, (750, 750))
# Load and scale background images for different screens
menu = pygame.image.load("menuScreen.jpg").convert_alpha()  # Load menu screen background
menu = pygame.transform.scale(menu, (750, 750))  # Scale to fit window
decide = pygame.image.load("decideScreen.jpg").convert_alpha()  # Load decision screen background
decide = pygame.transform.scale(decide, (750, 750))  # Scale to fit window
throwingPos = pygame.image.load("menuScreen.jpg").convert_alpha()  # Load action screen background
throwingPos = pygame.transform.scale(throwingPos, (750, 750))  # Scale to fit window

selectedSide=""  # Variable to store the selected side
# stores the player shots 
playerXCord = 0 
playerYCord = 0
#stores the locatioj of the target object 
objectXCord = 2
objectYCord = 2


# Wall properties
wall_width = 20  # Width of the wall
wall_height = height // 2 + 30  # 1/3 of the screen height
wall_x = 245 - wall_width // 2  # Center the wall on the screen
wall_y = height - wall_height  # Position the wall vertically in the middle

# Calculate the width of the score segments to the right of the wall
segment_width = (width - (wall_x + wall_width)) / 5

message_displayed = False  # Global variable to track message display state
landing_segment = 0  # Track which segment the ball lands in

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
                    bg = throwingPos  # Change background to action screen
                    selectedSide = "Granny"  # Set selected side to Granny
                    print(selectedSide)
                elif kidButton.collidepoint(event.pos):  # If "Child" button is pressed
                    bg = throwingPos  # Change background to action screen
                    selectedSide = "Child"  # Set selected side to Child
                    print(selectedSide)
            
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
                if message_displayed:
                    playerYCord = landing_segment
                    weapon.x = 50  # Optionally reset the projectile's position
                    weapon.y = 600
                    print('shot y cord = ' + str(landing_segment))
                    print(playerXCord, 'playerYCord = ', landing_segment)
                    if playerXCord == objectXCord and objectYCord == landing_segment:
                        print('hit!')
                        bg = throwingPos
                    else:
                        print('miss!')
                     # Reset message display state and allow for a new shot without moving the projectile
                    message_displayed = False
                    
                else:
                    pos = pygame.mouse.get_pos()
                    weapon.shootProjectile(pos)
                    

        
            
    
    
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
    
    # Button hover effects and display logic for throwingPos screen
    elif bg == throwingPos:
        window.blit(throwingPosExplainer, (width // 2 - throwingPosExplainer.get_width() // 2, 60))
        if throwingPosButton1.x <= a <= throwingPosButton1.x + 138 and throwingPosButton1.y <= b <= throwingPosButton1.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton1)  # Highlight throwingPosButton1 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton1)  # Default =throwingPosButton1 button appearance
        window.blit(throwingPosText1,(throwingPosButton1.x + 5, throwingPosButton1.y + 5))  # Draw '1' text on button

        if throwingPosButton2.x <= a <= throwingPosButton2.x + 138 and throwingPosButton2.y <= b <= throwingPosButton2.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton2)  # Highlight throwingPosButton2 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton2)  # Default =throwingPosButton2 button appearance
        window.blit(throwingPosText2,(throwingPosButton2.x + 5, throwingPosButton2.y + 5))  # Draw '2' text on button

        if throwingPosButton3.x <= a <= throwingPosButton3.x + 138 and throwingPosButton3.y <= b <= throwingPosButton3.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton3)  # Highlight throwingPosButton3 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton3)  # Default =throwingPosButton3 button appearance
        window.blit(throwingPosText3,(throwingPosButton3.x + 5, throwingPosButton3.y + 5))  # Draw '3' text on button

        if throwingPosButton4.x <= a <= throwingPosButton4.x + 138 and throwingPosButton4.y <= b <= throwingPosButton4.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton4)  # Highlight throwingPosButton4 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton4)  # Default =throwingPosButton4 button appearance
        window.blit(throwingPosText4,(throwingPosButton4.x + 5, throwingPosButton3.y + 5))  # Draw '4' text on button

        if throwingPosButton5.x <= a <= throwingPosButton5.x + 138 and throwingPosButton5.y <= b <= throwingPosButton5.y + 60:
            pygame.draw.rect(window, (180,180,180), throwingPosButton5)  # Highlight throwingPosButton5 on hover
        else:
            pygame.draw.rect(window, (110,110,110), throwingPosButton5)  # Default =throwingPosButton5 button appearance
        window.blit(throwingPosText5,(throwingPosButton5.x + 5, throwingPosButton5.y + 5))  # Draw '5' text on button

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
        
        


    weapon.update()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
