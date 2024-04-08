import pygame
pygame.init()

width = 750
height = 750
window = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Georgia', 40, bold=True)

start = font.render('Start', True, (255,255,255))
decideText = font.render('Whose side will you take?!', True, (255,255,255))
granny = font.render('Granny', True, (255,255,255))
child = font.render('Child', True, (255,255,255))

button = pygame.Rect(200,200,110,60)
grannyButton = pygame.Rect(500,300,170,60)
kidButton = pygame.Rect(500, 400, 170, 60)

menu = pygame.image.load("menuScreen.jpg").convert_alpha()
menu = pygame.transform.scale(menu, (750, 750))
decide = pygame.image.load("decideScreen.jpg").convert_alpha()
decide = pygame.transform.scale(decide, (750, 750))
throwing = pygame.image.load("throwingScreen.jpg").convert_alpha()
throwing = pygame.transform.scale(throwing, (750, 750))

selectedSide=""

bg = menu
run = True
while run:
    window.blit(bg, bg.get_rect())
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if bg == menu:
                if button.collidepoint(events.pos):
                    bg = decide
            elif bg == decide:
                if grannyButton.collidepoint(events.pos):
                    bg = throwing
                    selectedSide = "Granny"
                elif kidButton.collidepoint(events.pos):
                    bg = throwing
                    selectedSide = "Child"

    a, b = pygame.mouse.get_pos()
    if bg == menu: 
        if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
            pygame.draw.rect(window, (180,180,180), button)
        else:
            pygame.draw.rect(window, (110,110,110), button)
        window.blit(start,(button.x + 5, button.y + 5))
    elif bg == decide:
        if grannyButton.x <= a <= grannyButton.x + 170 and grannyButton.y <= b <= grannyButton.y + 60:
            pygame.draw.rect(window, (180,180,180), grannyButton)
        else:
            pygame.draw.rect(window, (110,110,110), grannyButton)
        window.blit(granny,(grannyButton.x + 5, grannyButton.y + 5))
        if kidButton.x <= a <= kidButton.x + 170 and kidButton.y <= b <= kidButton.y + 60:
            pygame.draw.rect(window, (180,180,180), kidButton)
        else:
            pygame.draw.rect(window, (110,110,110), kidButton)
        window.blit(child,(kidButton.x + 5, kidButton.y + 5))

    pygame.display.update()
