import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# general constants
running = True

# colors
black = (0,0,0)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(black)
  pygame.display.flip()
pygame.quit()
