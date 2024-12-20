import pygame 
pygame.init()
window = pygame.display.set_mode((600,650))
window.fill((230,230,230))
NavyBlue = (0,0,230)
pygame.draw.circle(window,NavyBlue,(400,400),50)
pygame.draw.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()