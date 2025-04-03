from config import SCREEN_SIZE, BG_COLOR
import pygame 
class Canvas: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Kepler Problem")

        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60

             
    def update(self): 
        pass 

    
    def render(self): 
        self.screen.fill(BG_COLOR)

        pygame.display.flip()
        self.clock.tick(self.fps)
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def run(self):
        while(self.running): 
            self.update()
            self.handle_events()
            self.render()


        
