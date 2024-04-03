import pygame
pygame.init()

width = 750
height = 750
window = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Georgia', 40, bold=True)
surf = font.render('Quit', True, (255,255,255))
button = pygame.Rect(200,200,110,60)

run = True
while run:
    window.fill((0,0,0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                print("quit")
    
    a, b = pygame.mouse.get_pos() 
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
        pygame.draw.rect(window, (180,180,180), button)
    else:
        pygame.draw.rect(window, (110,110,110), button)
    window.blit(surf,(button.x + 5, button.y + 5))

    pygame.display.update()
