import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        xmole, ymole = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    xmouse, ymouse = event.pos
                    if xmole <= xmouse < xmole + 32 and ymole <= ymole < ymole + 32:
                        xmole = random.randrange(0, 20) * 32
                        ymole = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range(21):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))
            for j in range(17):
                pygame.draw.line(screen, "black", (0, j * 32), (640, j * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(xmole, ymole)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
