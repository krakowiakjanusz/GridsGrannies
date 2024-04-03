# Welcome text.


# Player chooses grannies or children to play as.


# Display battleship-style grid.


# Ask for an input of which square to place an item on.


# Do that 5 times.


# Randomly populate the squares of the opposing team.


# Display 5 x-axis positions to shoot from.


# Choose position.


# Display 5 y-axis positions to hit.


# Choose position.
import pygame
import math

# display window variables
width = 750
height = 750

# display window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("projectile's second attempt")

# projectile motion class
class projectiles(object):
    # initialises projectile
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    # draws the projectile
    def draw(self, window):
        pygame.draw.circle(window, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius-1)

    # movement of the projectile
    def path(startx, starty, power, angle, time):
        # velocity
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        # distance
        distx = velx * time
        # for y - have to use motion with downwards acceleration (gravity!!)
        # -4.9 acts as gravity --- should be -9.8 however -4.9 provides smoother motion
        disty = (vely * time) + ((-4.9 * (time)**2)/2)

        # new x and y
        newx = round(distx + startx)
        newy = round(starty - disty)

        return (newx, newy)

# refreshes screen
def drawingScreen():
    window.fill((64,64,64))
    weapon.draw(window)
    pygame.draw.line(window, (255,255,255), line[0], line[1])
    pygame.display.update()

# determines the angle of the projectile
def findAngle(pos):
    sX = weapon.x
    sY = weapon.y
    
    # tangents the weapons coordinates to figure out the length of the power line
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        # if it can't find the tangent
        angle = math.pi / 2

    # determines direction the projetile is moving in - sections the screen into four 
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle
    
    return angle

# destroyer of grannies and children
weapon = projectiles(300, 744, 5, (255,255,255))

# variables to do with projectile movement
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

# gameloop
run = True
while run:
    # while projectile is in motion
    if shoot:
        # checks projectile is moving on the screen
        if weapon.y < 750 - weapon.radius:
            time += 0.05
            po = projectiles.path(x, y, power, angle, time)
            weapon.x = po[0]
            weapon.y = po[1]
        else:
            # stops projectile falling off screen
            shoot = False
            weapon.y = 744

        # stops projectile running off screen
        if weapon.x > 750 - weapon.radius:
            shoot = False
            weapon.x = 744
        if weapon.x < 0 + weapon.radius:
            shoot = False
            weapon.x = 6

    # line that follows off the projectile
    pos = pygame.mouse.get_pos()
    line = [(weapon.x, weapon.y),pos]
    drawingScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quits game
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # shots fired
            if shoot == False:
                shoot = True
                x = weapon.x
                y = weapon.y
                time = 0
                # determines power of throw on the length of the line coming off the projectile - longer line = more power
                power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/8
                # calls angle function between the mouse and the ball
                angle = findAngle(pos)
            
pygame.quit()

# Display hit or miss message.


# Opposing team does their turn.


# Display hit or miss message.


# Loop until win or lose condition is met.


# 'You win' screen. 


# Restart prompt.
